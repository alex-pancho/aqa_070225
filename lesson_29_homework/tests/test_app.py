from lesson_29_homework.app import app
import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    app.create_table()
    yield


def test_insert_user():
    app.insert_user("Alice")
    users = app.get_users()
    assert any(u[1] == "Alice" for u in users)


def test_update_user():
    users = app.get_users()
    user_id = users[0][0]
    app.update_user(user_id, "Bob")
    updated_user = app.get_users()[0]
    assert updated_user[1] == "Bob"


def test_delete_user():
    users = app.get_users()
    user_id = users[0][0]
    app.delete_user(user_id)
    users_after = app.get_users()
    assert len(users_after) == 0
