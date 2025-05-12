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

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')
    conn.commit()

def insert_sample_data():
    categories = [
        ("Electronics",),
        ("Books",),
        ("Clothing",)
    ]
    cursor.executemany('''
        INSERT INTO categories (name) VALUES (?)
    ''', categories)

    products = [
        ("Smartphone", "Android phone with 128GB storage", 299.99, 1),
        ("Laptop", "15 inch, 16GB RAM", 899.99, 1),
        ("Python Book", "Learn Python Programming", 39.99, 2),
        ("T-Shirt", "Cotton, Size M", 19.99, 3),
        ("Jeans", "Blue denim", 49.99, 3)
    ]
    cursor.executemany('''
        INSERT INTO products (name, description, price, category_id)
        VALUES (?, ?, ?, ?)
    ''', products)

    conn.commit()

def show_products_with_categories():
    query = '''
        SELECT products.name, products.description, products.price, categories.name AS category
        FROM products
        JOIN categories ON products.category_id = categories.id
    '''
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    show_products_with_categories()
    conn.close()