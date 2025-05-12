"""
Створіть базу даних для інтернет-магазину з наступними таблицями:
products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
categories: таблиця для категорій продуктів.
products повинна мати зовнішній ключ на таблицю categories.
Напишіть SQL-скрипт для створення зазначених таблиць.
Внесіть декілька рядків даних в кожну таблицю
Виконайте JOIN-запит, який повертає інформацію про продукти та назву їх категорій
"""

import sqlite3


def create_database():
    # Підключення до бази даних (створення, якщо не існує)
    conn = sqlite3.connect("internet_store.db")
    cursor = conn.cursor()

    # Створення таблиці categories
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """
    )

    # Створення таблиці products
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """
    )
    conn.close()


def insert_data_categories(*args: str) -> None:
    """
    Inserts multiple category names into the 'categories' table of the SQLite database.

    Args:
        *args: A variable number of category names (strings) to be added to the table.

    Functionality:
        - Connects to the 'internet_store.db' database.
        - Executes an INSERT statement for each category name provided in the arguments.
        - Commits the changes to the database.
        - Closes the database connection.

    Example:
        insert_data_categories('Electronics', 'Books', 'Clothing')
    """
    conn = sqlite3.connect("internet_store.db")
    cursor = conn.cursor()

    # Перевірка типу вхідних даних
    if not all(isinstance(i, str) for i in args):
        raise ValueError("ValueError: All category names must be strings.")

    # Внесення даних у таблицю categories
    for i in args:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (i,))
    # Збереження змін та закриття з'єднання
    conn.commit()
    conn.close()


def insert_data_products(*args: tuple) -> None:
    """
    Inserts multiple product records into the 'products' table of the SQLite database.

    Args:
        *args: A variable number of tuples, where each tuple contains the following:
            - name (str): The name of the product.
            - description (str): A brief description of the product.
            - price (float): The price of the product.
            - category_id (int): The ID of the category to which the product belongs.

    Functionality:
        - Connects to the 'internet_store.db' database.
        - Executes an INSERT statement for each product record provided in the arguments.
        - Commits the changes to the database.
        - Closes the database connection.

    Example:
        insert_data_products(
            ('Smartphone', 'Latest model', 699.99, 1),
            ('Laptop', 'High performance', 1299.99, 1),
            ('Python Programming', 'Learn Python', 29.99, 2),
            ('T-Shirt', 'Comfortable cotton t-shirt', 19.99, 3)
        )
    """
    conn = sqlite3.connect("internet_store.db")
    cursor = conn.cursor()

    # Перевірка типу вхідних даних
    for i in args:
        if not (
            isinstance(i, tuple)
            and len(i) == 4
            and isinstance(i[0], str)
            and isinstance(i[1], str)
            and isinstance(i[2], (float, int))
            and isinstance(i[3], int)
        ):
            raise ValueError(
                "ValueError: Each product must be a tuple (name: str, description: str, price: float, category_id: int)."
            )

    # Внесення даних у таблицю products
    for i in args:
        cursor.execute(
            "INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)",
            i,
        )
    # Збереження змін та закриття з'єднання
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    insert_data_categories("Electronics", "Books", "Clothing")
    insert_data_products(
        ("Smartphone", "Latest model", 699.99, 1),
        ("Laptop", "High performance", 1299.99, 1),
        ("Python Programming", "Learn Python", 29.99, 2),
        ("T-Shirt", "Comfortable cotton t-shirt", 19.99, 3),
    )

    # Виконання JOIN-запиту
    conn = sqlite3.connect("internet_store.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT products.name, categories.name
        FROM products
        JOIN categories ON products.category_id = categories.id
    """
    )
    results = cursor.fetchall()
    for row in results:
        print(f"Product: {row[0]}, Category: {row[1]}")
    conn.close()
