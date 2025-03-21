import unittest
import os
import time

from homework_11 import log_event

class MyTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('login_system.log'):
            os.remove('login_system.log')

    def read_last_line(self):
        with open('login_system.log', 'r') as file:
            lines = file.readlines()
            return lines[-1] if lines else ""

    def test_success_log(self):
        log_event("Emma", "success")
        time.sleep(0.1)
        last_line = self.read_last_line()
        self.assertIn("Username: Emma, Status: success", last_line)

    def test_expired_log(self):
        log_event("Oleh", "expired")
        last_line = self.read_last_line()
        self.assertIn("Username: Oleh, Status: expired", last_line)

    def test_failed_log(self):
        log_event("Olena", "failed")
        last_line = self.read_last_line()
        self.assertIn("Username: Olena, Status: failed", last_line)

    def test_unknown_status_log(self):
        log_event("George", "unknown")
        last_line = self.read_last_line()
        self.assertIn("Username: George, Status: unknown", last_line)

# Запуск тестів
if __name__ == '__main__':
    unittest.main()


