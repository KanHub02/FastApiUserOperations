from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum




class OperationKind(str, Enum):
    INCOMES = 'income'
    OUTCOME = 'outcomes'


class OperationBase(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]


class Operations(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass

class OperationUpdate(OperationBase):
    pass
