import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            dbname="my_database",
            user="postgres",
            password="test",
            host="db",
            port="5432"
        )
    except Exception as e:
        print("Connection failed:", e)
        return None

def create_table(connection, cursor, table_name, columns_name_type_dict):
    columns_name_type = []
    for name, type_ in columns_name_type_dict.items():
        columns_name_type.append(f"{name} {type_}")
    columns = ", ".join(columns_name_type)

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns}
        )
    ''')
    connection.commit()

def insert_products(connection, cursor,values):
    for record in values:
        try:
            test_price_value = float(record[2])
            cursor.execute('''
                INSERT INTO products (product_name, description, price, category_id)
                VALUES (%s, %s, %s, %s)
            ''', record)
            connection.commit()
        except Exception as e:
            print(f" Error inserting product {record}: {e}")
            connection.rollback() 

def insert_categories(connection, cursor, categories_value):
    for category in categories_value:
        try:
            cursor.execute('''
                INSERT INTO categories (category)
                VALUES (%s)
            ''', category)
            connection.commit()
        except Exception as e:
            print(f" Error inserting category {category}: {e}")
            connection.rollback()  

def update_product(connection, cursor, product_name, new_price):
    cursor.execute("UPDATE products SET price = %s WHERE product_name = %s", (new_price, product_name))
    connection.commit()

def delete_product(connection, cursor, product_name):
    cursor.execute("DELETE FROM products WHERE product_name = %s", (product_name,))
    connection.commit()

def select_all(cursor, table):
    cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()

