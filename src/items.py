from fastapi import APIRouter
from schemas import Item
from db import get_async_pool

items = APIRouter(prefix="/items")

pool = get_async_pool()



@items.post("")
async def add_item(item: Item):
    async with pool.connection() as conn:
        await conn.execute(
            "insert into items (order_id, name, price, number) values (%s, %s, %s, %s)",
            [int(item.order_id), item.name, item.price, item.number]
        )

@items.get("/{item_id}")
async def get_item(item_id: int):
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("select * from items where id = %i", [item_id])
        records = await cur.fetchall()
        return records


