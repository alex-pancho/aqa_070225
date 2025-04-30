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

conn = sqlite3.connect('eshop.db')

cursor = conn.cursor()

def create_tables(cursor, create_cmd):#, product_id, product_name, product_desc, price)
    cursor.execute(create_cmd)
    conn.commit()
        
def insert_into_categories(cursor, category_name):
    cursor.execute('''
        INSERT INTO categories (category_name) VALUES (?)
    ''', (category_name,))
    conn.commit()
    
def insert_into_products(cursor, category_id, product_name, product_desc, price):
    cursor.execute('''
        INSERT INTO products (category_id, product_name, product_desc, price) VALUES (?, ?, ?, ?)
    ''', (category_id, product_name, product_desc, price))
    conn.commit()
    
def select_all(cursor, select_cmd:str):
    cursor.execute(select_cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
if __name__ == "__main__":
    create_cmd_cat = ''' CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY,
        category_name TEXT
        )'''
    create_tables(cursor, create_cmd_cat)
    create_cmd = ''' CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        category_id INTEGER,
        product_name TEXT,
        product_desc TEXT,
        price DECIMAL,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )'''
    create_tables(cursor, create_cmd)
    insert_into_categories(cursor, 'electronics')
    insert_into_categories(cursor, 'books')
    insert_into_categories(cursor, 'clothing')
    
    insert_into_products(cursor, 1, "phone", "phone_desc", 99.99)
    insert_into_products(cursor, 2, "book", "book_desc", 9.99)
    insert_into_products(cursor, 3, "t-shirt", "cloth_desc", 19.99)
    select_all_cmd = "SELECT * FROM products" 
    select_all(cursor, select_all_cmd)
    select_cmd_cat = "SELECT * FROM categories" 
    select_all(cursor, select_cmd_cat)
    select_cmd = """SELECT products.product_id, products.product_name, products.price  FROM products 
    INNER JOIN categories ON products.category_id = categories.category_id;"""
    select_all(cursor, select_cmd)

    
    
    
