import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, Table, UUID
from sqlalchemy.dialects.postgresql import TIMESTAMP

from education_time_management.db.base import metadata

user = Table(
    "user",
    metadata,
    Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String, nullable=False),
    Column("is _active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
