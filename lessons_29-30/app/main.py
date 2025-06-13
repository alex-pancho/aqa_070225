from db import create_table, insert_user, update_user, delete_user, fetch_users

def main():
    create_table()
    insert_user("Alice", "alice@example.com")
    insert_user("Bob", "bob@example.com")
    update_user(1, "Alice Updated")
    delete_user(2)
    users = fetch_users()
    print("Users:", users)

if __name__ == "__main__":
    main()
