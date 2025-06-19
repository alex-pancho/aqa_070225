import sqlite3


def create_tables():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    # Створення таблиці категорій
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    # Створення таблиці продуктів
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)

    conn.commit()
    conn.close()


def insert_sample_data():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    # Перевірка чи є вже категорії
    cursor.execute("SELECT COUNT(*) FROM categories")
    category_count = cursor.fetchone()[0]

    if category_count == 0:
        categories = [("Електроніка",), ("Одяг",), ("Книги",)]
        cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)
        print("Категорії додано.")
    else:
        print("Категорії вже існують. Пропуск вставки.")

    # Перевірка чи є вже продукти
    cursor.execute("SELECT COUNT(*) FROM products")
    product_count = cursor.fetchone()[0]

    if product_count == 0:
        products = [
            ("Смартфон", "Сучасний телефон з камерою", 7999.99, 1),
            ("Ноутбук", "Потужний ноутбук для роботи", 19999.50, 1),
            ("Футболка", "Чорна футболка з логотипом", 299.99, 2),
            ("Роман", "Історичний роман українською", 159.00, 3)
        ]
        cursor.executemany(
            "INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)",
            products
        )
        print("Продукти додано.")
    else:
        print("Продукти вже існують. Пропуск вставки.")

    conn.commit()
    conn.close()


def get_products_with_categories():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT products.name, products.description, products.price, categories.name AS category
        FROM products
        JOIN categories ON products.category_id = categories.id
    """)

    results = cursor.fetchall()
    conn.close()
    return results


# Приклад виконання
if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    data = get_products_with_categories()
    print("\nСписок продуктів з категоріями:")
    for row in data:
        print(f"Продукт: {row[0]}, Опис: {row[1]}, Ціна: {row[2]} грн, Категорія: {row[3]}")
