from datetime import datetime
from sqlalchemy import String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class SyncRecord(Base):
    __tablename__ = "sync_records"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    device_id: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    client_record_id: Mapped[int] = mapped_column(nullable=False)
    record_uuid: Mapped[str] = mapped_column(
        String(36), unique=True, index=True, nullable=False
    )
    payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )