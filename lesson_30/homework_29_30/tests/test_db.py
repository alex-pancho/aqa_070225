from homework_29_30 import main

def test_db_operations():
    main.create_table()
    main.insert_item("Test")
    items = main.get_items()
    assert any("Test" in str(row) for row in items)

    main.update_item("Test", "Updated")
    items = main.get_items()
    assert any("Updated" in str(row) for row in items)

    main.delete_item("Updated")
    items = main.get_items()
    assert all("Updated" not in str(row) for row in items)
