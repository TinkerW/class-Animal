from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    mall: str
    address: str

class Banks(BaseModel):
    name: str
    rating: float
    opened: int

class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: bool

class Balance(BaseModel):
    card: Cards
    amount: float
    currency: str
