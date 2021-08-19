import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_sparkify_db():
    """Creates sparkify_db database, connects and places cursor on sparkify_db
    database.
    """
    # connect to default database
    conn = psycopg2.connect("user=postgres \
                            host=127.0.0.1 \
                            port=5432 \
                            dbname=postgres_db \
                            password=passryme1")
    cur = conn.cursor()
    conn.set_session(autocommit=True)

    # create sparkify_db database
    cur.execute("""DROP DATABASE IF EXISTS sparkify_db""")
    cur.execute("""CREATE DATABASE sparkify_db""")

    # close intial connection
    conn.close()
    cur.close()

    # connect to sparkify_db
    conn = psycopg2.connect("user=postgres \
                            host=127.0.0.1 \
                            port=5432 \
                            dbname=sparkify_db \
                            password=passryme1")
    cur = conn.cursor()

    return conn, cur


def create_table(conn, cur):
    """Creates tables in sparkify_db database by running all create table queries
    defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def drop_table(conn, cur):
    """Drops tables in sparkify_db database by running all drop table queries
    defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Driver main function.
    """
    conn, cur = create_sparkify_db()

    drop_table(conn, cur)
    print("Table dropped successfully!")

    create_table(conn, cur)
    print("Table created successfully!")

    # close connection and cursor
    conn.close()
    cur.close()


if __name__ == "__main__":
    main()
