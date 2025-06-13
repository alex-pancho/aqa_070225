import unittest
from db import create_table, insert_user, update_user, delete_user, fetch_users

class TestApp(unittest.TestCase):
    def setUp(self):
        create_table()

    def test_insert_and_fetch(self):
        insert_user("Test", "test@example.com")
        users = fetch_users()
        self.assertTrue(any("Test" in user for user in users))

    def test_update(self):
        insert_user("UpdateTest", "update@example.com")
        users = fetch_users()
        user_id = users[-1][0]
        update_user(user_id, "UpdatedName")
        users = fetch_users()
        self.assertTrue(any("UpdatedName" in user for user in users))

    def test_delete(self):
        insert_user("DeleteTest", "delete@example.com")
        users = fetch_users()
        user_id = users[-1][0]
        delete_user(user_id)
        users = fetch_users()
        self.assertFalse(any(user[0] == user_id for user in users))

if __name__ == "__main__":
    unittest.main()
