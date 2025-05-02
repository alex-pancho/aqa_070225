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


def create_table(cursor, table_name, fields: dict):
    """
    Створює таблицю з вказаною назвою та полями.
    :param cursor: курсор sqlite3
    :param table_name: назва таблиці
    :param fields: словник з полями, де ключ — ім'я поля, а значення — SQL-тип
    """
    field_definitions = ", ".join([f"{name} {definition}" for name, definition in fields.items()])
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({field_definitions});"
    cursor.execute(sql)


def insert_into_table(cursor, table_name, data: list[dict]):
    """
    Універсальна функція для вставки даних у таблицю.
    :param cursor: курсор sqlite3
    :param table_name: назва таблиці
    :param data: список словників, де ключ — назва поля, значення — значення
    """
    if not data:
        return

    fields = data[0].keys()
    field_names = ", ".join(fields)
    placeholders = ", ".join(["?" for _ in fields])
    insert_cmd = "INSERT OR IGNORE"
    sql = f"{insert_cmd} INTO {table_name} ({field_names}) VALUES ({placeholders})"
    values = [tuple(item[field] for field in fields) for item in data]
    cursor.executemany(sql, values)


conn = sqlite3.connect("homework.db")
cursor = conn.cursor()

categories_fields = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "name": "TEXT NOT NULL UNIQUE"
}

products_fields = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "name": "TEXT NOT NULL",
    "description": "TEXT",
    "price": "REAL NOT NULL",
    "category_id": "INTEGER",
    "FOREIGN KEY(category_id)": "REFERENCES categories(id)"
}

create_table(cursor, "categories", categories_fields)
create_table(cursor, "products", products_fields)

if __name__ == "__main__":

    insert_into_table(cursor, "categories", [
        {"name": "Електроніка"},
        {"name": "Ігри"},
        {"name": "Книги"}
    ])

    insert_into_table(cursor, "products", [
        {"name": "Смартфон", "description": "Новий смартфон", "price": 1001.00, "category_id": 1},
        {"name": "Футболка Пікачу", "description": "Зручна футболка", "price": 25.00, "category_id": 2},
        {"name": "Роман", "description": "Цікавий роман", "price": 13.49, "category_id": 3}
    ])

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Створені таблиці:", tables)
    cursor.execute("""
    SELECT products.name, products.description, products.price, categories.name AS category
    FROM products
    JOIN categories ON products.category_id = categories.id;
    """)
    conn.commit()
    results = cursor.fetchall()
    if results:
        print("JOIN пройшов успішно. Результати:")
        for row in results:
            print(row)
    else:
        print("JOIN не повернув жодних результатів.")
    conn.close()
