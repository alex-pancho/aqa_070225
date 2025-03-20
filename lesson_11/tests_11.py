import unittest
from homework_11 import log_event

class TestLogEvent(unittest.TestCase):

    def test_1_log_event_success(self):
        """Тестування логування для успішного входу"""
        with self.assertLogs(level='INFO') as log:
            log_event('user1', 'success')
            # Перевіряємо, чи є в логах повідомлення з 'success'
            self.assertIn('Login event - Username: user1, Status: success', log.output[0])

    def test_2_log_event_expired(self):
        """Тестування логування для застарілого пароля"""
        with self.assertLogs(level='WARNING') as log:
            log_event('user2', 'expired')
            # Перевіряємо, чи є в логах повідомлення з 'success'
            self.assertIn('Login event - Username: user2, Status: expired', log.output[0])
  
    def test_3_log_event_error(self):
        """Тестування логування для невірного пароля"""
        with self.assertLogs(level="ERROR") as log:
            log_event('user3', 'error')
            self.assertIn('Login event - Username: user3, Status: failed', log.output[0])
 

if __name__ == "__main__":
    unittest.main(verbosity=2)