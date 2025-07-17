from sqlalchemy.orm import Session
from datetime import date
from src import models


def get_stocks(db: Session, skip: int=0, limit: int=100,week: date=None):
    query= db.query(models.Stock)
    if week:
        query= query.filter(models.Stock.date_time == week)
    return query.offset(skip).limit(limit).all()

def get_stock_id(db: Session, stock_id: int):
    return db.query(models.Stock).filter(models.Stock.stocks_id == stock_id).first()

def get_stocks_count(db: Session):
    query= db.query(models.Stock)
    return query.count()