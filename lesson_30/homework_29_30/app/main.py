from db import get_connection

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT);")

def insert_item(name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO items (name) VALUES (%s);", (name,))

def update_item(old_name, new_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE items SET name=%s WHERE name=%s;", (new_name, old_name))

def delete_item(name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM items WHERE name=%s;", (name,))

def get_items():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM items;")
            return cur.fetchall()
