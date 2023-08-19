from datetime import datetime


from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, DECIMAL

metadata = MetaData()


orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("created_date", TIMESTAMP, default=datetime.utcnow),
    Column("updated_date", TIMESTAMP, default=datetime.utcnow),
    Column("title", String, nullable=False),
    Column("total", DECIMAL),
    Column("items", JSON)
)


items = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", DECIMAL, nullable=False),
    Column("number", Integer, nullable=False)
)

stats = Table(
    "stats",
    metadata,
    Column("total_orders", Integer, default=0),
    Column("total_order_price", DECIMAL, default=0.0),
    Column("avg_order_price", DECIMAL, default=0.0),
    Column("total_items", Integer, default=0),
    Column("avg_items", DECIMAL, default=0),
    Column("most_ordered_item", String)
)



