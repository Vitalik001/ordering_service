import asyncio
from fastapi import FastAPI

from fastapi_app.models.orders import orders
from fastapi_app.models.items import items
from fastapi_app.db_connection.database_config import get_async_pool

app = FastAPI(
    title="ordering service"
)

pool = get_async_pool()

async_pool = get_async_pool()

app.include_router(orders)
app.include_router(items)

async def check_async_connections():
    while True:
        await asyncio.sleep(600)
        print("check async connections")
        await async_pool.check()


@app.on_event("startup")
async def startup():
    asyncio.create_task(check_async_connections())
    # async with pool.connection() as conn:
    #     await conn.execute("CREATE DATABASE postgres")
    #     await conn.execute("CREATE TABLE IF NOT EXISTS orders (\
    #             id SERIAL PRIMARY KEY,\
    #             created_date DATE NOT NULL DEFAULT CURRENT_DATE,\
    #             updated_date DATE NOT NULL DEFAULT CURRENT_DATE,\
    #             title VARCHAR(255) NOT NULL,\
    #             total DECIMAL(10, 2) NOT NULL);")

@app.get("/", tags=["operations"])
async def root():
    return "Ordering service"