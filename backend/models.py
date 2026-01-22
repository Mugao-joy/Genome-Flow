from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True)
    external_id = Column(String)
    organism = Column(String)
    tissue = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
