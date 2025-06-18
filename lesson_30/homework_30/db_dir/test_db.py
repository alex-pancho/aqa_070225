import pytest
from . import db

@pytest.fixture(scope="module")
def db_fixt():
    connection = db.get_connection()
    if connection is None:
        pytest.fail("Database connection failed. Is PostgreSQL running?")
    cursor = connection.cursor()
    # Створюємо таблиці один раз на модуль
    db.create_table(connection, cursor, "categories", {
        "id": "SERIAL PRIMARY KEY",
        "category": "TEXT UNIQUE"
    })
    db.create_table(connection, cursor, "products", {
        "id": "SERIAL PRIMARY KEY",
        "product_name": "TEXT UNIQUE",
        "description": "TEXT",
        "price": "FLOAT",
        "category_id": "INTEGER",
        "FOREIGN KEY(category_id)": "REFERENCES categories(id)"
    })
    yield connection, cursor


    # Після всіх тестів видаляємо таблиці
    cursor.execute('DROP TABLE IF EXISTS products CASCADE;')
    cursor.execute('DROP TABLE IF EXISTS categories CASCADE;')
    connection.commit()

    cursor.close()
    connection.close()

def test_connection(db_fixt):
    connection, _ = db_fixt
    assert connection is not None

def test_insert_categories(db_fixt):
    connection, cursor = db_fixt
    db.insert_categories(connection, cursor, ([("fruits",), ("dairy",)]))
    cursor.execute("SELECT * FROM categories WHERE category = %s", ("fruits",))
    result = cursor.fetchone()
    assert result is not None

def test_insert_product(db_fixt):
    connection, cursor = db_fixt
    db.insert_products(connection, cursor, ([
        ("banana", "yellow", "69.99", 1),
        ("milk", "lactose free", 64.99, 2),
        ("cheese", "brie", 479.99, 2),
        ("apple", "green", 55, 1)
    ]))
    cursor.execute("SELECT * FROM products WHERE product_name = %s", ("banana",))
    result = cursor.fetchone()
    assert result is not None

def test_update_product(db_fixt):
    connection, cursor = db_fixt
    db.update_product(connection, cursor, "apple", 99.99)
    cursor.execute("SELECT price FROM products WHERE product_name = 'apple'")
    result = cursor.fetchone()
    assert result[0] == 99.99

def test_delete_product(db_fixt):
    connection, cursor = db_fixt
    db.delete_product(connection, cursor, "apple")
    cursor.execute("SELECT * FROM products WHERE product_name = 'apple'")
    result = cursor.fetchone()
    assert result is None

def test_select_all(db_fixt):
    connection, cursor = db_fixt
    results = db.select_all(cursor, "products")
    assert isinstance(results, list)