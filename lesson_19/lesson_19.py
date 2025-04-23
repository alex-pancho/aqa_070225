import sqlite3


# Підключення до бази даних (створює файл БД, якщо він не існує)
conn = sqlite3.connect('example.db')

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS access (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date_time TEXT
    )
''')


# Збереження змін у базі даних
conn.commit()
# Оновлення даних
# cursor.execute('''
#     UPDATE users SET email = ? WHERE username = ?
# ''', ('john.doe@example.com', 'Dmytro'))
# conn.commit()

# Видалення даних
# cursor.execute('DELETE FROM users WHERE username = ?', ('Dmytro',))
# conn.commit()
# Вставка даних
# cursor.execute('''
#     INSERT INTO users (username, email) VALUES (?, ?)
# ''', ('Rostik', 'rostik@gmail.com'))
# # Збереження змін у базі даних
# conn.commit()

select_user_cmd = "SELECT * FROM users" # where email like '%gmail.com%'
def select_print(cursor, select_cmd:str):
    cursor.execute(select_cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

select_print(cursor, select_user_cmd)

def insert_access_info(cursor, user_id, date_time):
    cursor.execute('''
        INSERT INTO access (user_id, date_time) VALUES (?, ?)
    ''', (user_id, date_time))
    # Збереження змін у базі даних
    conn.commit()

def iter_insert(cursor, my_list:list):
    for val in my_list:
        user_id, date_time = val
        insert_access_info(cursor, user_id, date_time)

userlog = [
    (3, "20250403T124546.7456784"),
    (3, "20250403T124547.7456784"),
    (3, "20250403T125547.7456784"),
    (4, "20250403T124546.7456784"),
    (1, "20250403T124546.7456784"),
    (2, "20250404T125547.7456784"),
    (5, "20250404T125547.7456784"),
    (2, "20250404T124546.7456784"),
    (1, "20250404T124547.7456784"),
    (4, "20250404T125547.7456784"),
]

#iter_insert(cursor, userlog)

select_access = 'SELECT * FROM access'
select_print(cursor, select_access)

select_cmd = """SELECT username, email, date_time, user_id, users.id FROM access 
RIGHT JOIN users ON access.user_id = users.id;"""
select_print(cursor, select_cmd)