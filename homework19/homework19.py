import sqlite3

"""
    Створіть базу даних для інтернет-магазину з наступними таблицями:

    products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
    products: повинна мати зовнішній ключ на таблицю categories.
    categories: таблиця для категорій продуктів.
    
    Напишіть функції:
    1. для створення зазначених таблиць.
    2. Для Внесення декілька рядків даних в кожну таблицю
    3. JOIN-запит для повернення інформації про продукти та назву їх категорій

    Здати ЯК ПР. 
    Файл бази в ПР не включати.
"""

def create_tables(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY,
            category TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            price FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

def insert_category(cursor, category):
    cursor.execute('''
        INSERT INTO categories (category) VALUES (?)
    ''', (category,))

def insert_product(cursor, name, description, price, category_id):
    cursor.execute('''
        INSERT INTO products (name, description, price, category_id)
        VALUES (?, ?, ?, ?)
    ''', (name, description, price, category_id))

def get_products_with_categories(cursor):
    cursor.execute('''
        SELECT
            products.name,
            products.description,
            products.price,
            categories.category
        FROM products
        JOIN categories ON products.category_id = categories.id
    ''')
    return cursor.fetchall()

if __name__ == "__main__":
    connection = sqlite3.connect("homework19.db")
    cursor = connection.cursor()

    create_tables(cursor)

    categories = ["clothes", "electronics", "books"]
    for category in categories:
        insert_category(cursor, category)

    cursor.execute("SELECT id, category FROM categories")
    rows = cursor.fetchall()

    category_name_to_id = {}
    for category_id, category_name in rows:
        category_name_to_id[category_name] = category_id

    insert_product(cursor, "Jeans", "Blue denim jeans", 49.99, category_name_to_id["clothes"])
    insert_product(cursor, "Smartphone", "Latest Android phone", 699.00, category_name_to_id["electronics"])
    insert_product(cursor, "Headphones", "Wireless noise-canceling", 129.50, category_name_to_id["electronics"])
    insert_product(cursor, "Novel", "Mystery fiction book", 14.25, category_name_to_id["books"])
    insert_product(cursor, "Sweater", "Wool winter sweater", 59.90, category_name_to_id["clothes"])
    insert_product(cursor, "E-reader", "Electronic book reader", 85.99, category_name_to_id["electronics"])

    products = get_products_with_categories(cursor)
    for product in products:
        print(product)

    connection.commit()
    connection.close()