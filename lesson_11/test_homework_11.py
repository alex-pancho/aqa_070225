from aqa_070225.lesson_11.homework import log_event
import unittest


class TestLogEvent(unittest.TestCase):

    file_path = "login_system.log"

    def check_last_line(self, text):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                if lines and text in lines[-1]:
                    return True
                return False
        except FileNotFoundError:
            print(f"Файл {self.file_path} не знайдено.")
            return False
        except Exception as e:
            print(f"Помилка: {e}")
            return False

    def test_01(self):
        log_event("John", "success")
        text = "Login event - Username: John, Status: success"
        self.assertTrue(self.check_last_line(text))

    def test_02(self):
        log_event("John", "expired")
        text = "Login event - Username: John, Status: expired"
        self.assertTrue(self.check_last_line(text))

    def test_03(self):
        log_event("John", "failed")
        text = "Login event - Username: John, Status: failed"
        self.assertTrue(self.check_last_line(text))

    def test_04(self):
        with self.assertRaises(TypeError):
            log_event(123, "success")

    def test_05(self):
        with self.assertRaises(TypeError):
            log_event("John", 123)

    def test_06(self):
        with self.assertRaises(ValueError):
            log_event("", "success")

    def test_07(self):
        with self.assertRaises(ValueError):
            log_event("John", "")
