import time
import psycopg2
import pytest

def wait_for_db(host, port, retries=10, delay=1):
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
    ...

@pytest.fixture(scope="module")
def db_connection():
    """Establishes a connection to the Postgres DB and creates a test table."""
    try:
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
        print("\nDatabase connection closed.")

    except psycopg2.OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")

def test_connection(db_connection):
    """Test: Connection to database is successful."""
    assert db_connection is not None and not db_connection.closed

def test_insert_and_select(db_connection):
    """Test: Insert and read a user from the database."""
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", ('John Wick',))
    db_connection.commit()

    cursor.execute("SELECT name FROM users WHERE name = %s", ('John Wick',))
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == 'John Wick'

def test_update(db_connection):
    """Test: Update user name."""
    cursor = db_connection.cursor()
    cursor.execute("UPDATE users SET name = %s WHERE name = %s", ('Neo', 'John Wick'))
    db_connection.commit()

    cursor.execute("SELECT name FROM users WHERE name = %s", ('Neo',))
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == 'Neo'

def test_delete(db_connection):
    """Test: Delete user from database."""
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM users WHERE name = %s", ('Neo',))
    db_connection.commit()

    cursor.execute("SELECT * FROM users WHERE name = %s", ('Neo',))
    result = cursor.fetchone()

    assert result is None