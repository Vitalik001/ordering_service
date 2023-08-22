from fastapi import APIRouter
import datetime
import schemas
from db import get_async_pool

orders = APIRouter(prefix="/orders")

pool = get_async_pool()

@orders.post("")
async def add_order(order: schemas.Order):
    async with pool.connection() as conn:
        total = 0 #get total value
        await conn.execute(
            "insert into orders (created_date, updated_date, title, total) values (%s, %s, %s, %s)",
            [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), order.title, total],
        )


@orders.get("")
async def get_orders():
    async with pool.connection() as conn, conn.cursor() as cur:
        await cur.execute("select * from orders")
        records = await cur.fetchall()
        return records


# POST /orders - create a new order
# @app.post("/orders", response_model=List[Order], tags=["operations"])
# async def add_order(order: Order, session: AsyncSession = Depends(get_async_session)):
#     orders.append(order)
#     return orders

# GET /orders/<id>/items - list items of a single order
# @app.get("/orders/{id}/items", response_model=List[Item])
# async def get_items(id: int):
#     return orders[id].items


# # GET /orders/<id>/items/<id> - get a single order item
# @app.get("/orders/{order_id}/items/{item_id}", response_model=Item)
# async def get_items(order_id: int, item_id: int):
#     return [item for item in orders[order_id] if item.id == item_id]
#
#
# # POST /orders/<id>/items - add an item to an order
# @app.post("/orders/{id}/items", response_model=List[Item])
# async def add_item(item: Item):
#     orders[id].items.append(item)
#     return orders[id].items
#
#
# # PUT /orders/<id>/items/<id> - update existing order item
# @app.put("/orders/{order_id}/items/{item_id}", response_model=List[Item])
# async def update_item(order_id: int, item_id: int):
#     for item in orders[order_id].items:
#         if item.id == item_id:
#             # update item
#             return orders[id].items
#
#
# # DELETE /orders/<id>/items/<id> - delete existing order item
# @app.delete("orders/{order_id}/items/{item_id}", response_model=List[Item])
# async def delete_item(order_id: int, item_id: int):
#     for item in orders[order_id].items:
#         if item.id == item_id:
#             del item
#             return orders[id].items
#
#
# # GET /orders - list all orders
# @app.get("orders", response_model=List[Order])
# async def get_orders():
#     return orders
#
#
# # GET /orders/<id> - get a single order
# @app.get("/orders/{id}", response_model=Order)
# async def get_order(id: int):
#     return orders[id]
#
#

#
#
# # PUT /orders/<id> - update existing order
# @app.put("orders/{id}", response_model=List[Order])
# async def update_order(id: int):
#     # update order
#     return orders
#
#
# # DELETE /orders/<id> - delete existing order
# @app.delete("/orders/{id}", response_model=List[Order])
# async def delete_order(id: int):
#     for order in orders:
#         if order.id == id:
#             del order
#             return orders
#
#
# # GET /stats - return general stats
# @app.get("/stats", response_model=Stats)
# async def get_stats():
#     return stats