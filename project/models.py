""" Application status models """
from apistar.backends.sqlalchemy_backend import Session
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from project.utils import GUID

Base = declarative_base()

class ApplicationStatus(Base):
    __tablename__ = "environment_status"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, default=False)
    group = Column(String)
    last_updated = Column(DateTime(timezone=True), default=func.now())
