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

# Підключення до бази даних (створює файл БД, якщо він не існує)
conn = sqlite3.connect("internet_store.db")
cursor = conn.cursor()

"""1. Функція для створення зазначених таблиць."""


def create_tables():
    # Створення таблиці категорій
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    # Створення таблиці продуктів з зовнішнім ключем на categories
    cursor.execute('''
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


# дані для вставки в таблиці
categories_data = [
    ("Продукти",),
    ("Одяг",),
    ("Техніка",)
]
# дані для вставки в таблиці
products_data = [
    ("Банани", "Фрукти вагові", 50, 1),
    ("Сукня", "Чорна сукня розміру М", 900, 2),
    ("Ноутбук", "Dell", 25556, 3)
]


def insert_data(categories: list, products: list):
    cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)
    cursor.executemany(
        "INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)",
        products
    )
    conn.commit()


def get_products_with_categories():
    cursor.execute('''
        SELECT products.name, products.description, products.price, categories.name AS category_name
        FROM products
        JOIN categories ON products.category_id = categories.id
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(f"Продукт: {row[0]}, Опис: {row[1]}, Ціна: {row[2]} грн, Категорія: {row[3]}")


if __name__ == "__main__":
    create_tables()
    insert_data(categories_data, products_data)
    get_products_with_categories()

    conn.close()
