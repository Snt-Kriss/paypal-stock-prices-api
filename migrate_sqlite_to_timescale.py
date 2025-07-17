import os
import sqlite3

from sqlalchemy.orm import Session
from src import models
from src.database import Base
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

sqlite_path= "./stock.db"
sqlite_conn= sqlite3.connect(sqlite_path)
sqlite_cursor= sqlite_conn.cursor()

#Read data from SQLite
sqlite_cursor.execute("SELECT * FROM stocks")
rows= sqlite_cursor.fetchall()

#postgres setup
pg_url= os.getenv("DATABASE_URL")
pg_engine= create_engine(pg_url)
Base.metadata.create_all(pg_engine)

#insert into postgresql
with Session(pg_engine) as session:
    for row in rows:
        stock= models.Stock(
            stocks_id= row[0],
            date_time= row[1],
            open=row[2],
            high=row[3],
            low=row[4],
            close=row[5],
            adjusted_close=row[6],
            volume=row[7],
        )
        session.add(stock)
    session.commit()

print(f"Migrated {len(rows)} rows from SQLite to TimescaleDB")

sqlite_conn.close()