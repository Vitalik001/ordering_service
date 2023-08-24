import datetime
from http.client import HTTPException

from fastapi import APIRouter

from fastapi_app.db_connection.database_config import get_async_pool
from .schemas import Order, Item

orders = APIRouter(prefix="/orders")

pool = get_async_pool()


@orders.get("")
async def get_orders():
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("select * from orders")
        records = await cur.fetchall()
        return records



# GET /orders/<id> - get a single order
@orders.get("/{id}")
async def get_order(id: int):
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("select * from orders where id = %s", [id])
        records = await cur.fetchall()
        return records

@orders.post("")
async def add_order(order: Order):
    async with pool.connection() as conn:
        total = 0 #get total value
        await conn.execute(
            "insert into orders (created_date, updated_date, title, total) values (%s, %s, %s, %s)",
            [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), order.title, total],
        )


# PUT /orders/<id> - update existing order
@orders.put("/{order_id}")
async def update_order(order_id: int, updated_order: Order):
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("SELECT * FROM orders WHERE id = %s", [order_id])
        existing_order = await cur.fetchall()
        if existing_order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        total = 0  # Calculate the new total value here

        await conn.execute(
            "UPDATE orders SET title = %s, total = %s, updated_date = %s WHERE id = %s",
            [updated_order.title,
            total,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            order_id]
        )
        return {"message": "Order updated successfully"}

# DELETE /orders/<id> - delete existing order
@orders.delete("/{order_id}")
async def delete_order(order_id: int):
    async with pool.connection() as conn, conn.cursor() as cur:
        # Check if the order exists
        await cur.execute("SELECT * FROM orders WHERE id = %s", [order_id])
        existing_order = await cur.fetchall()
        if existing_order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        # Delete the order from the database
        await conn.execute("DELETE FROM orders WHERE id = %s", [order_id])
        return {"message": "Order deleted successfully"}



# GET /orders/<id>/items - list items of a single order
@orders.get("/{id}/items")
async def get_order_items(id: int):
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("select * from items where order_id = %s", [id])
        records = await cur.fetchall()
        return records


# # GET /orders/<id>/items/<id> - get a single order item
@orders.get("/{order_id}/items/{item_id}")
async def get_order_item(order_id: int, item_id: int):
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("select * from items where order_id = %s and id = %s", [order_id, item_id])
        records = await cur.fetchall()
        return records


# # POST /orders/<id>/items - add an item to an order
@orders.post("/{id}/items")
async def add_item(id: int, item: Item):
    async with pool.connection() as conn:
        await conn.execute(
            "insert into items (order_id, name, price, number) values (%s, %s, %s, %s)",
            [id, item.name, item.price, item.number]
        )


# # PUT /orders/<id>/items/<id> - update existing order item
@orders.put("/{order_id}/items/{item_id}")
async def update_order_item(order_id: int, item_id: int, updated_item: Item):
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("SELECT * FROM items WHERE id = %s AND order_id = %s", [item_id, order_id])
        existing_item = await cur.fetchall()
        if existing_item is None:
            raise HTTPException(status_code=404, detail="Item not found")

        total = 0  # Calculate the new total value here

        await conn.execute(
            "UPDATE items SET name = %s, price = %s, number = %s WHERE id = %s",
            [updated_item.name,
            updated_item.price,
            updated_item.number,
            item_id]
        )
        return {"message": "Item updated successfully"}
#
#
# # DELETE /orders/<id>/items/<id> - delete existing order item
@orders.delete("/{order_id}/items/{item_id}")
async def delete_order_item(order_id: int, item_id: int):
    async with pool.connection() as conn, conn.cursor() as cur:
        # Check if the order exists
        await cur.execute("SELECT * FROM items WHERE id = %s AND order_id = %s", [item_id, order_id])
        existing_item = await cur.fetchall()
        if existing_item is None:
            raise HTTPException(status_code=404, detail="Item not found")

        # Delete the order from the database
        await conn.execute("DELETE FROM items WHERE id = %s AND order_id = %s", [item_id, order_id])
        return {"message": "Item deleted successfully"}

