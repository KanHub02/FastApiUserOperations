import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operations(Base):
    __tablename__ = "operations"

    id = sql.Column(sql.Integer, primary_key=True)
    date = sql.Column(sql.Date)
    kind = sql.Column(sql.String)
    amount = sql.Column(sql.Numeric(10, 2))
    description = sql.Column(sql.String)
