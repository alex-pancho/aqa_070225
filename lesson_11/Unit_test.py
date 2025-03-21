from homework_11 import log_event
import unittest

class TestHW11(unittest.TestCase):

    def test_01(self):
        """Тест успішного входу"""
        try:
            log_event("User123", "success")
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    def test_02(self):
        """Тест закінчення терміну дії пароля"""
        try:
            log_event("User123", "expired")
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    def test_03(self):
        """Тест невірного пароля"""
        try:
            log_event("User123", "failed")
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    def test_04(self):
        """Тест для невідомого статусу (перевіряємо, що функція не падає)"""
        try:
            log_event("User123", "unknown")
            result = True
        except Exception:
            result = False
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)