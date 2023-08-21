import uuid
from typing import List

from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    id: int = uuid.uuid4()
    order_id: int
    name: str
    price: float
    number: int


class Stats(BaseModel):
    total_orders: int
    total_order_price: float
    avg_order_price: float
    total_items: int
    avg_items: float
    most_ordered_item: str


class Order(BaseModel):
    id: int = uuid.uuid4()
    created_date: datetime
    updated_date: datetime
    title: str
    total: float
    items: List[Item]
