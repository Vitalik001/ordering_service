import asyncio
from fastapi import FastAPI

from orders import orders
from items import items
from db import get_async_pool

app = FastAPI(
    title="ordering service"
)


async_pool = get_async_pool()

app.include_router(orders)
app.include_router(items)

async def check_async_connections():
    while True:
        await asyncio.sleep(600)
        print("check async connections")
        await async_pool.check()


@app.on_event("startup")
def startup():
    asyncio.create_task(check_async_connections())

@app.get("/", tags=["operations"])
async def root():
    return "Ordering service"