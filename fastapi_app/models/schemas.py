from pydantic import BaseModel


class Item(BaseModel):
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
    title: str
