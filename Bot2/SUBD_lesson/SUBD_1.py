import psycopg2
from config import *

try:
    # CONNECT to existed DB
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    connection.autocommit = True
    # Cursor for perform DB operations cursor = connection.cursor()
    cursor = connection.cursor()

    with connection.cursor() as cur:
        cur.execute(
            "SELECT filename FROM media WHERE id=5;"
        )
        print(f"Server version: {cur.fetchone()}")

    with connection.cursor() as cur:
        # DELETE !!
        cur.execute(
            '''DROP TABLE users;'''
        )

    print('[INFO] Success Droped')

except Exception as _ex:
    print('[INFO] FATAL Error while working with PostgreSQL!!!', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] Connection closed!!!')
