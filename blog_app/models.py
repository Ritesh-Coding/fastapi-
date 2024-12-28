from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True,nullable=False,index=True)
    title = Column(String,nullable=False)
    body = Column(String,nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))