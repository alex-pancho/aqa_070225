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
import sqlite3


conn = sqlite3.connect('homework19.db')

cursor = conn.cursor()

def create_tables(cursor) -> None:
    """
    Function to create tables in the database.
    Creates two tables: categories and products.
    """
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            category_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            description TEXT,
            price FLOAT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    ''')

    conn.commit()

def insert_category(cursor, id: int, category_name: str) -> None:
    """
    Function to insert a category into the categories table.
    """
    cursor.execute('''
        INSERT INTO categories (id, category_name) VALUES (?, ?)
    ''', (id, category_name))
    conn.commit()

def insert_product(cursor, id: int, product_name: str, description: str, price: float, category_id: int) -> None:
    """
    Function to insert a product into the products table.
    """
    cursor.execute('''
        INSERT INTO products (id, product_name, description, price, category_id) VALUES (?, ?, ?, ?, ?)
    ''', (id, product_name, description, price, category_id))
    conn.commit()

def select_products_with_categories(cursor) -> None:
    """
    Function to select products along with their categories using LEFT JOIN.
    """
    cursor.execute('''
        SELECT product_name, description, price, categories.id, category_name
        FROM products
        RIGHT JOIN categories ON products.category_id = categories.id
    ''')
    results = cursor.fetchall()
    for row in results:
        print(f"Product Name: {row[0]}, Description: {row[1]}, Price: {row[2]}, Category ID: {row[3]}, Category Name: {row[4]}")

if __name__ == "__main__":
    create_tables(cursor)
    insert_category(cursor, 1, 'Books')
    insert_category(cursor, 2, 'Electronics')
    insert_category(cursor, 3, 'Clothing')
    insert_category(cursor, 4, 'Home & Kitchen')
    insert_category(cursor, 5, 'Toys & Games')
    insert_product(cursor, 1, 'Kobzar', 'Poetry book by Taras Shevchenko', 359.50, 1)
    insert_product(cursor, 2, '1984', 'Dystopian novel by George Orwell', 299.99, 1)
    insert_product(cursor, 3, 'Smartphone X200', 'Modern smartphone with AMOLED display', 8999.99, 2)
    insert_product(cursor, 4, 'Wireless Headphones', 'Noise-cancelling over-ear headphones', 2199.00, 2)
    insert_product(cursor, 5, 'Classic T-shirt', 'Cotton, unisex, black', 299.00, 3)
    insert_product(cursor, 6, 'Denim Jacket', 'Blue denim jacket, slim fit', 899.00, 3)
    insert_product(cursor, 7, 'Non-stick Frying Pan', '28cm pan with ceramic coating', 449.00, 4)
    insert_product(cursor, 8, 'Blender 500W', 'Compact blender for smoothies and sauces', 1199.00, 4)
    insert_product(cursor, 9, 'LEGO Classic', 'Creative brick box, 500+ pieces', 1299.00, 5)
    insert_product(cursor, 10, 'Board Game: Catan', 'Popular strategy board game', 1099.00, 5)
    select_products_with_categories(cursor)