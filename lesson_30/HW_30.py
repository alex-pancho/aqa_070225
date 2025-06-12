import pytest
import psycopg2

@pytest.fixture(scope="module")
def db_connection():
    """Створює підключення до БД для тестів та закриває його після."""
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
        cursor.execute("CREATE TABLE users (id INT, name VARCHAR(255));")
        conn.commit()
        
        yield conn
        
        conn.close()
        print("\nПідключення до БД закрито.")
        
    except psycopg2.OperationalError as e:
        pytest.fail(f"ПОМИЛКА ПІДКЛЮЧЕННЯ ДО БД: {e}")

def test_database_connection(db_connection):
    """Тест 1: Перевіряє, що підключення успішне."""
    print("\n[Тест 1] Перевірка з'єднання...")
    assert db_connection is not None and not db_connection.closed
    print("[Тест 1] Успішно!")

def test_data_insertion_and_selection(db_connection):
    """Тест 2: Перевіряє вставку та вибірку даних."""
    print("\n[Тест 2] Вставка та перевірка даних...")
    cursor = db_connection.cursor()
    
    cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (1, 'John Wick'))
    db_connection.commit()
    
    cursor.execute("SELECT name FROM users WHERE id=%s", (1,))
    result = cursor.fetchone()
    
    assert result is not None
    assert result[0] == 'John Wick'
    print("[Тест 2] Успішно!")