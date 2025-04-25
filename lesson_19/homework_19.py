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
# Підключення до бази 
import sqlite3

conn = sqlite3.connect('online_store')
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

def create_table(table_name, columns_name_type_dict):
    # функція для створення таблиці з колонками заданими як словник {назва колонки: тип}
    columns_name_type =  []
    for names, types in columns_name_type_dict.items():
        column = f"{names} {types}"
        columns_name_type.append(column)
    columns = ", ".join(columns_name_type)
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        {columns})
    ''')
    conn.commit()

def insert_products(values):
    #Вставка продуктів 
    for record in values:
        try:
            test_price_value = float(record[2])
            cursor.execute('''
                    INSERT INTO products (product_name, description, price, category_id) 
                    VALUES (?, ?, ?, ?)
                ''',record)
            conn.commit()
        except Exception as e:
                print(f"Error occured when try to insert {record}: {e}")
        
def insert_categories(categories_value):
    #Вставка категорій 
    for category in categories_value:
        try:
            cursor.execute('''
                INSERT INTO categories (category) 
                VALUES (?)
            ''',category)
            conn.commit()
        except Exception as e:
            print(f"Error occured when try to insert {category}: {e}")

def join_print():
    # Вивід продуктів разом із категоріями
    cursor.execute('''SELECT product_name, description, price, c.category FROM products p
                   JOIN categories as c
                   ON p.category_id == c.id ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    

def select_all_print(table):
    # Вивід усіх записів з обраної таблиці
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__== "__main__":
    
    create_table("categories", {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
        "category": "TEXT UNIQUE"})
    
    create_table("products", {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
            "product_name": "TEXT UNIQUE",
            "description":"TEXT",
            "price": "FLOAT", 
            "category_id": "INTEGER",
            "FOREIGN KEY(category_id)": "REFERENCES categories(id)"})
    
    insert_categories([("fruits",), ("dairy",)])

    insert_products([("banana", "yellow", "69.99", 1),
                     ("milk", "lactose free", 64.99, 2),
                     ("pork", "organic", 239.01, 3),
                     ("cheese", "brie", 479.99, 2),
                     ("apple", "green", 55, 1)])
    
    select_all_print("products")
    print("_____________\n")
    select_all_print("categories")
    print("_____________\n")
 
    insert_categories([("meat",)])
    insert_products([("pork", "organic", 239.01, 3)])
    select_all_print("products")
    print("_____________\n")
    select_all_print("categories")
    print("_____________\n")

    join_print()