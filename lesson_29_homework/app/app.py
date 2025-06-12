import psycopg2


def connect():
    return psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )


def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL
                );
            """)
        conn.commit()


def insert_user(name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name) VALUES (%s);", (name,))
        conn.commit()


def update_user(user_id, new_name):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE users SET name = %s WHERE id = %s;", (new_name, user_id))
        conn.commit()


def delete_user(user_id):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        conn.commit()


def get_users():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            return cur.fetchall()