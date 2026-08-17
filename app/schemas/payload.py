from typing import Any, Dict, List
from pydantic import BaseModel, Field


class RecordItem(BaseModel):
    client_record_id: int
    record_uuid: str
    payload: Dict[str, Any]


class BatchSyncRequest(BaseModel):
    device_id: str
    records: List[RecordItem]


class SyncResponseItem(BaseModel):
    client_record_id: int
    record_uuid: str
    status: str


class BatchSyncResponse(BaseModel):
    processed_count: int
    skipped_count: int
    results: List[SyncResponseItem]