import psycopg2

def get_connection():
    return psycopg2.connect(
        host="db",
        database="testdb",
        user="testuser",
        password="testpass"
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT
    );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);", (name, email))
    conn.commit()
    cur.close()
    conn.close()

def update_user(user_id, name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name = %s WHERE id = %s;", (name, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def fetch_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
