from fastapi import Depends, HTTPException
from src import crud, schemas
from src.database import SessionLocal
from fastapi import FastAPI
from datetime import date
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API health check successful"}


@app.get("/v0/stocks/", response_model= list[schemas.StockSchema])
def read_stocks(skip: int=0, limit: int=100, week: date=None, db: Session= Depends(get_db)):
    stocks= crud.get_stocks(db, skip=skip, limit=limit, week=week)

    return stocks

@app.get("/v0/stocks/{stock_id}", response_model=schemas.StockSchema)
def read_stock_id(stock_id: int, db: Session= Depends(get_db)):
    stock= crud.get_stock_id(db, stock_id=stock_id)
    if stock is None:
        raise HTTPException(status_code= 404, detail= "Not found")
    else:
        return stock

@app.get("/v0/stocks/counts", response_model= schemas.Count)
def get_count(db: Session= Depends(get_db)):
    counts= schemas.Count(
        stock_count= crud.get_stocks_count(db)
    )

    return counts