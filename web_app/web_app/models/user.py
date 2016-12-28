from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
)

from sqlalchemy import DateTime
from sqlalchemy.sql.expression import func
from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    dsnr = Column(Unicode, unique=True)
    first_name = Column(Unicode, nullable=False)
    last_name = Column(Unicode, nullable=False)
    phone_nr = Column(Unicode)
    type = Column(Unicode, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    



