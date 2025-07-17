from sqlalchemy import Column, Integer, Float, Date
from src.database import Base

class Stock(Base):
    __tablename__ = "stocks"

    stocks_id = Column(Integer, primary_key=True, index=True)
    date_time = Column(Date)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adjusted_close = Column(Float)
    volume = Column(Integer)

