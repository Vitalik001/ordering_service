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
                COUNT(DISTINCT o.id) AS total_orders,\
                SUM(o.total) AS total_order_price,\
                AVG(o.total) AS avg_order_price,\
                SUM(i.number) AS total_items,\
                AVG(i.number) AS avg_items,\
                (\
                    SELECT name\
                    FROM (\
                        SELECT\
                            name,\
                            ROW_NUMBER() OVER (ORDER BY SUM(number) DESC) AS rn\
                        FROM items\
                        GROUP BY name\
                    ) ranked\
                    WHERE rn = 1\
                ) AS most_ordered_item\
            FROM orders o\
            LEFT JOIN items i ON o.id = i.order_id;"
            )
            result = await cur.fetchall()
            print(result)
            if None in result[0]:
                return {"message": "please, add some items"}

            statistics = {
                "total_orders": result[0][0],
                "total_order_price": float(result[0][1]),
                "avg_order_price": float(result[0][2]),
                "total_items": result[0][3],
                "avg_items": float(result[0][4]),
                "most_ordered_item": result[0][5]
            }
    return statistics
