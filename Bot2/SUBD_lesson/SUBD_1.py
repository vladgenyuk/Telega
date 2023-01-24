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

    # -------------------
    # cur.execute()
    # --------------------CREATE TABLE users(
    #     # id serial PRIMARY KEY,
    #     # first_name varchar(50) NOT NULL,
    #     # nickname varchar(50) NOT NULL)
    # create new table
    # cur.execute(
    #     '''INSERT INTO users (first_name, nickname) VALUES
    #     ('OLEG', 'KYKAPACHA');
    #
    #     '''
    # )
    # print('[INFO] Success')
    # -------------------
    # cur.execute(
    #     '''SELECT nickname FROM users WHERE first_name = 'OLEG' ;'''
    # )
    # print(f'Olegs name is: {cur.fetchone()[0]}')

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
