import unittest

from lesson_11.homework_11 import log_event


class TestLogger(unittest.TestCase):
    log_file = 'login_system.log'

    def check_logs_file(self, text):
        """Функція пошуку тексту в лог файлі"""
        try:
            with open(self.log_file, 'r') as file:
                lines = file.readlines()
                return any(text in line for line in lines)
        except FileNotFoundError:
            print(f"Файл {self.log_file} не знайдено.")
            return False

    def test_01_log_success(self):
        """Тестування логування для успішного входу"""
        with self.assertLogs(level='INFO') as log:
            log_event('Tetiana', 'success')
            self.assertIn('Login event - Username: Tetiana, Status: success', log.output[0]), "Logs not working"

    def test_02_log_expired(self):
        """Тестування логування для застарілого пароля"""
        with self.assertLogs(level='WARNING') as log:
            log_event('Tetiana', 'expired')
            self.assertIn('Login event - Username: Tetiana, Status: expired', log.output[0]), "Logs not working"

    def test_03_log_error(self):
        """Тестування логуваня з невалідними данними"""
        with self.assertLogs(level="ERROR") as log:
            log_event('Tetiana', 'error')
            self.assertIn('Login event - Username: Tetiana, Status: error', log.output[0]), "Logs not working"

    def test_04_empty_data(self):
        """ Тест на роботу методу з порожніми значеннями імені та прізвища """
        with self.assertRaises(TypeError):
            log_event(), "Невалідні дані користувача"

    def test_05_logfile(self):
        """ Тест на наявність запису у лог-файлі """
        log_event("Tetiana", "success")
        text = "Login event - Username: Tetiana, Status: success"
        self.assertFalse(self.check_logs_file(text)), "Текст не записаний у лог файл"


if __name__ == "__main__":
    unittest.main(verbosity=2)
