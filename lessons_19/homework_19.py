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

def create_tables():
    conn = sqlite3.connect('store.db')
    cur = conn.cursor()

    cur.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )

    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect('store.db')
    cur = conn.cursor()

    categories = [
        ('Електроніка',),
        ('Одяг',),
        ('Книги',)
    ]
    cur.executemany("INSERT INTO categories (name) VALUES (?)", categories)

    products = [
        ('Ноутбук', 'Lenovo IdeaPad 5', 24000.00, 1),
        ('Футболка', 'Біла чоловіча футболка', 400.00, 2),
        ('Python для початківців', 'Книга про Python', 350.00, 3),
        ('Навушники', 'Bluetooth-гарнітура', 1200.00, 1)
    ]
    cur.executemany("INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)", products)

    conn.commit()
    conn.close()

def get_products_with_categories():
    conn = sqlite3.connect('store.db')
    cur = conn.cursor()

    cur.execute('''
        SELECT products.name, products.description, products.price, categories.name AS category
        FROM products
        JOIN categories ON products.category_id = categories.id
    ''')

    results = cur.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    create_tables()
    insert_sample_data()

    print("Продукти з категоріями:\n")
    for product in get_products_with_categories():
        print(f"Назва: {product[0]} | Опис: {product[1]} | Ціна: {product[2]} грн | Категорія: {product[3]}")

