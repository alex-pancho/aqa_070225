import unittest
from homework_11 import log_event

username = "DorVit"
status_1 = "successs"
status_2 = "failed"
status_3 = "expired"


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
        log_event(username, status_1)
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: {status_1}", last_log)

    def test_2_failed(self):
        """
        Тест перевіряє логін з невірним паролем та логується на рівні error
        """
        log_event(username, status_2)
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: {status_2}", last_log)

    def test_3_expired(self):
        """
        Тест перевіряє логін з застарілим паролем та логується на рівні warning
        """
        log_event(username, status_3)
        last_log = self.read_log()
        self.assertIn(f"Username: {username}, Status: {status_3}", last_log)

    def test_4_different_users(self):
        """
        Тест перевіряє логін з застарілим паролем одразу пысля успішного логіну та логується на рівні warning
        """
        log_event(username, status_1)
        log_event("user456", status_2)
        last_log = self.read_log()
        self.assertIn(f"Username: user456, Status: {status_2}", last_log)

    def test_5_empty_username(self):
        """
        Тест перевіряє логін з порожнім ім'ям користувача.
        """
        log_event("", status_2)
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