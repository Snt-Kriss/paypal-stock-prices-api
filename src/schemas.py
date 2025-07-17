from pydantic import BaseModel, ConfigDict
from datetime import date


class StockSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    stocks_id: int
    date_time: date
    open: float
    high: float
    low: float
    close: float
    adjusted_close: float
    volume: int


class Count(BaseModel):
    stock_count: int