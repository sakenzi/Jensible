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
from sqlalchemy.orm import relationship
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, nullable=False)



