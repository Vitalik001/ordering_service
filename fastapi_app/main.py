import asyncio
from fastapi import FastAPI

from fastapi_app.models.orders import orders
from fastapi_app.models.stats import stats
from fastapi_app.db_connection.database_config import get_async_pool

app = FastAPI(
    title="ordering service"
)

pool = get_async_pool()

async_pool = get_async_pool()

app.include_router(orders, tags=["orders"])
app.include_router(stats,  tags=["stats"])

async def check_async_connections():
    while True:
        await asyncio.sleep(600)
        print("check async connections")
        await async_pool.check()


@app.on_event("startup")
async def startup():
    asyncio.create_task(check_async_connections())

@app.get("/", tags=["main_page"])
async def root():
    return "Ordering service"