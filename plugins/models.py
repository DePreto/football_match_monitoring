from plugins.db import Base

from sqlalchemy import Column, Integer, JSON
from sqlalchemy.dialects.postgresql import TIMESTAMP


class NextMatches(Base):
    __tablename__ = "next_matches"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(TIMESTAMP(timezone=True))
    data = Column(JSON)

