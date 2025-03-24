from homework_11 import log_event
import unittest
from unittest.mock import patch

class TestHW11(unittest.TestCase):

    @patch('homework_11.logging.getLogger')
    def test_01(self, mock_logger):
        """Тест успішного входу"""
        log_event("User123", "success")
        mock_logger.return_value.info.assert_called_once_with("Login event - Username: User123, Status: success")

    @patch('homework_11.logging.getLogger')
    def test_02(self, mock_logger):
        """Тест закінчення терміну дії пароля"""
        log_event("User123", "expired")
        mock_logger.return_value.warning.assert_called_once_with("Login event - Username: User123, Status: expired")

    @patch('homework_11.logging.getLogger')
    def test_03(self, mock_logger):
        """Тест невірного пароля"""
        log_event("User123", "failed")
        mock_logger.return_value.error.assert_called_once_with("Login event - Username: User123, Status: failed")

    @patch('homework_11.logging.getLogger')
    def test_04(self, mock_logger):
        """Тест для невідомого статусу (перевіряємо, що функція не падає)"""
        log_event("User123", "unknown")
        mock_logger.return_value.error.assert_called_once_with("Login event - Username: User123, Status: unknown")

    @patch('homework_11.logging.getLogger')
    def test_05_empty_username(self, mock_logger):
        """Тест з порожнім ім'ям користувача"""
        log_event("", "success")
        mock_logger.return_value.info.assert_called_once_with("Login event - Username: , Status: success")

    @patch('homework_11.logging.getLogger')
    def test_06_large_username(self, mock_logger):
        """Тест з дуже довгим ім'ям користувача"""
        long_username = "User" * 100
        log_event(long_username, "success")
        mock_logger.return_value.info.assert_called_once_with(f"Login event - Username: {long_username}, Status: success")


if __name__ == "__main__":
    unittest.main(verbosity=2)