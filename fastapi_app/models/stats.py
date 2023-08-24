from fastapi import APIRouter

from fastapi_app.db_connection.database_config import get_async_pool

stats = APIRouter(prefix="/stats")

pool = get_async_pool()


# GET /stats - return general stats
@stats.get("")
async def get_stats():
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                "SELECT\
                    COUNT(o.id) AS total_orders,\
                    SUM(o.total) AS total_order_price,\
                    AVG(o.total) AS avg_order_price,\
                    SUM(i.number) AS total_items,\
                    AVG(i.number) AS avg_items,\
                    (\
                        SELECT name\
                        FROM items\
                        WHERE order_id = (\
                            SELECT order_id\
                            FROM items\
                            GROUP BY order_id\
                            ORDER BY SUM(number) DESC\
                            LIMIT 1\
                        )\
                        LIMIT 1\
                    ) AS most_ordered_item\
                FROM orders o\
                JOIN items i ON o.id = i.order_id;"
            )
            result = await cur.fetchall()
    return result
