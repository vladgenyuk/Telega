import asyncio

import psycopg2
from config import *


async def db_conn(id):
    try:
        connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True
        cursor = connection.cursor()
        with connection.cursor() as cur:
            cur.execute(
                f"SELECT filename FROM media WHERE id={id};"
            )
            print(cur.fetchone()[0])
            return cur.fetchone()
    except Exception as _ex:
        print('[INFO] FATAL Error while working with PostgreSQL!!!', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] Connection closed!!!')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db_conn(6))
    loop.close()
