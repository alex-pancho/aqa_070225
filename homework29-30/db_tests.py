import time
import psycopg2
import pytest

def wait_for_db(host, port, retries=10, delay=2):
    for _ in range(retries):
        try:
            conn = psycopg2.connect(
                dbname="test_db",
                user="test_user",
                password="test_password",
                host=host,
                port=port
            )
            conn.close()
            print("Database is ready!")
            return
        except psycopg2.OperationalError:
            print("Waiting for database...")
            time.sleep(delay)
    pytest.fail("Database connection failed after waiting.")

wait_for_db("db", 5432)

@pytest.fixture(scope="module")
def db_connection():
    """Connect to DB and prepare schema."""
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));")
    conn.commit()

    yield conn
    conn.close()
    print("DB connection closed.")

def test_connection(db_connection):
    assert db_connection is not None and not db_connection.closed

def test_insert_and_select(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", ('Gandalf Grey',))
    db_connection.commit()

    cursor.execute("SELECT name FROM users WHERE name = %s", ('Gandalf Grey',))
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == 'Gandalf Grey'

def test_update(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE name = %s", ('Bilbo', 'Gandalf Grey'))
    db_connection.commit()

    cursor.execute("SELECT name FROM users WHERE name = %s", ('Bilbo',))
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == 'Bilbo'

def test_delete(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM users WHERE name = %s", ('Bilbo',))
    db_connection.commit()

    cursor.execute("SELECT * FROM users WHERE name = %s", ('Bilbo',))
    result = cursor.fetchone()

    assert result is None