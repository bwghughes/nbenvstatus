""" Application status models """
from sqlalchemy import Boolean, Column, DateTime, Integer, String, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from apistar.backends.sqlalchemy_backend import Session
from slugify import slugify

Base = declarative_base()

class ApplicationStatus(Base):
    __tablename__ = "environment_status"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, default=False)
    group = Column(String)
    slug = Column(String)
    last_updated = Column(DateTime(timezone=True), default=func.now())

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

event.listen(ApplicationStatus.name, 'set', ApplicationStatus.generate_slug, retval=False)
