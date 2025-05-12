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

def create_table(cursor, create_cmd):
    cursor.execute(create_cmd)
    conn.commit()

def insert_category(cursor, category_name):
    cursor.execute('''
        INSERT INTO categories (category_name) VALUES (?)
    ''', (category_name,))
    conn.commit()

def insert_product(cursor, product_name, product_desc, product_price, category_id):
    cursor.execute('''
        INSERT INTO products (product_name, product_desc, product_price, category_id)
        VALUES (?, ?, ?, ?)
    ''', (product_name, product_desc, product_price, category_id))
    conn.commit()

def select_all(cursor, select_cmd):
    cursor.execute(select_cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    
    create_cmd_cat = '''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT
        )
    '''
    create_table(cursor, create_cmd_cat)

    create_cmd_prod = '''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            product_desc TEXT,
            product_price DECIMAL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    '''
    create_table(cursor, create_cmd_prod)

    insert_category(cursor, "home appliances")
    insert_category(cursor, "education")
    insert_category(cursor, "footwear")

    insert_product(cursor, "Blender", "Kitchen blender with 3 speeds", 49.99, 1)
    insert_product(cursor, "Math Workbook", "Exercises for grade 6 students", 12.50, 2)
    insert_product(cursor, "Sneakers", "Running shoes for everyday use", 39.90, 3)

    select_cmd = '''
        SELECT products.product_id, products.product_name, products.product_price, categories.category_name
        FROM products
        INNER JOIN categories ON products.category_id = categories.category_id
    '''
    select_all(cursor, select_cmd)

cursor.close()
conn.close()
