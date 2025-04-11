import unittest
from homework_11 import log_event

username = "DorVit"
success = "success"
failed = "failed"
expired = "expired"


class TestLogEvent(unittest.TestCase):

    def read_log(self):
        """
        Зчитує останній рядок із лог-файлу.
        """
        with open('login_system.log', 'r') as log:
            return log.readlines()[-1]

    def test_1_success(self):
        """
        Тест перевіряє успішний логін та логується на рівні інфо
        """
        log_event(username, success)
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: {success}", last_log)

    def test_2_failed(self):
        """
        Тест перевіряє логін з невірним паролем та логується на рівні error
        """
        log_event(username, failed)
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: {failed}", last_log)

    def test_3_expired(self):
        """
        Тест перевіряє логін з застарілим паролем та логується на рівні warning
        """
        log_event(username, expired)
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: {expired}", last_log)

    def test_4_different_users(self):
        """
        Тест перевіряє логін з застарілим паролем одразу пысля успішного логіну та логується на рівні warning
        """
        log_event(username, success)
        log_event("user456", failed)
        last_log = self.read_log()
        self.assertIn(f"Username: user456, Status: {failed}", last_log)

    def test_5_empty_username(self):
        """
        Тест перевіряє логін з порожнім ім'ям користувача.
        """
        log_event("", failed)
        last_log = self.read_log()
        self.assertIn("Username: , Status: failed", last_log)

    def test_6_empty_status(self):
        """
        Тест перевіряє логін з порожнім статусом.
        """
        log_event(username, "")
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: ", last_log)


if __name__ == "__main__":
    unittest.main(verbosity=2)