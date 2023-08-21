from http.client import HTTPException
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT  # <-- ADD THIS LINE
import asyncio
from fastapi import FastAPI
from schemas import *

app = FastAPI(
    title="ordering service"
)



@app.on_event("startup")
async def create_database():
    # await asyncio.sleep(10)
    con = psycopg2.connect(dbname="postgres", user="postgres", host="localhost", password="postgres")

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE

    cur = con.cursor()

    try:
        cur.execute(sql.SQL("CREATE DATABASE test;"))
    except:
        cur.execute(sql.SQL("DROP DATABASE test;"))
        cur.execute(sql.SQL("CREATE DATABASE test;"))

    db_con = psycopg2.connect(dbname="test", user="postgres", host="localhost", password="postgres")

    cur = db_con.cursor()
    db_con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS orders ( \
                            id SERIAL PRIMARY KEY, \
                            created_date DATE NOT NULL DEFAULT CURRENT_DATE,\
                            updated_date DATE NOT NULL DEFAULT CURRENT_DATE,\
                            title VARCHAR(255) NOT NULL,\
                            total DECIMAL(10, 2) NOT NULL);"))

    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS items (\
                        id SERIAL PRIMARY KEY,\
                        order_id INT REFERENCES orders(id),\
                        name VARCHAR(255) NOT NULL,\
                        price DECIMAL(10, 2) NOT NULL,\
                        number INT NOT NULL);"))


@app.get("/", tags=["operations"])
async def root():
    return "Ordering service"

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    db_con = psycopg2.connect(dbname="test", user="postgres", host="localhost", password="postgres")

    cur = db_con.cursor()
    db_con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    query = "SELECT * FROM items WHERE id = %s;"
    cur.execute(query, (item_id,))
    item = cur.fetchone()  # Assuming fetchone() fetches a single row

    if item is None:
        return {"message": "Item not found"}

    item_dict = {
        "item_id": item[0],
        "name": item[1],
        "price": item[2],
        "number": item[3]
    }

    return item_dict


@app.post("/items/")
async def create_item(item: Item):
    try:
        db_con = psycopg2.connect(dbname="test", user="postgres", host="localhost", password="postgres")

        cur = db_con.cursor()
        db_con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        query = "INSERT INTO items (name, price, number) VALUES (%s, %s, %s) RETURNING id;"
        cur.execute(query, (item.name, item.price, item.number))
        item_id = cur.fetchone()[0]  # Assuming id is the first column returned

        db_con.commit()
        return {"item_id": item_id, "message": "Item added successfully"}
    except Exception as e:
        db_con.rollback()
        raise HTTPException(status_code=500, detail=str(e))




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
