from sqlalchemy import (
    String,
    Integer,
    Text,
    Column,
    func,
    DateTime,
    ForeignKey,
    Float,
    Boolean,
    DECIMAL,
    Date,
)
from datetime import datetime
from sqlalchemy.orm import relationship
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    email_verified_at = Column(DateTime, default=datetime.utcnow)
    