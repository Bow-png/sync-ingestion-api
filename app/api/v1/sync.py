from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import verify_api_key
from app.database import get_db
from app.models.sync_record import SyncRecord
from app.schemas.payload import BatchSyncRequest, BatchSyncResponse, SyncResponseItem

router = APIRouter(prefix="/sync", tags=["Sync Engine"])


@router.post(
    "/batch",
    response_model=BatchSyncResponse,
    dependencies=[Depends(verify_api_key)],
)
async def ingest_batch(
    payload: BatchSyncRequest,
    db: AsyncSession = Depends(get_db),
):
    results = []
    processed_count = 0
    skipped_count = 0

    for item in payload.records:
        stmt = select(SyncRecord).where(SyncRecord.record_uuid == item.record_uuid)
        existing_record = await db.scalar(stmt)

        if existing_record:
            skipped_count += 1
            results.append(
                SyncResponseItem(
                    client_record_id=item.client_record_id,
                    record_uuid=item.record_uuid,
                    status="DUPLICATE_SKIPPED",
                )
            )
        else:
            new_record = SyncRecord(
                device_id=payload.device_id,
                client_record_id=item.client_record_id,
                record_uuid=item.record_uuid,
                payload=item.payload,
            )
            db.add(new_record)
            processed_count += 1
            results.append(
                SyncResponseItem(
                    client_record_id=item.client_record_id,
                    record_uuid=item.record_uuid,
                    status="CREATED",
                )
            )

    await db.commit()

    return BatchSyncResponse(
        processed_count=processed_count,
        skipped_count=skipped_count,
        results=results,
    )