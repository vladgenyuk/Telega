import psycopg2
from config import *
import asyncio


def db_conn(id):
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
                f"SELECT address FROM media WHERE id={id};"
            )
            return cur.fetchone()[0]
    except Exception as _ex:
        print('[INFO] FATAL Error while working with PostgreSQL!!!', _ex)
    finally:
        if connection:
            connection.close()


a = db_conn(3)
