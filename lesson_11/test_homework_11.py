from homework_11 import log_event
import unittest


class TestLogEvent(unittest.TestCase):

    def test_01_log_success(self):
        """Positive test log_event success status of logging"""
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("test_user", "success")
        self.assertIn("Login event - Username: test_user, Status: success", log.output[0])

    def test_02_log_expired(self):
        """Positive test log_event expired status of logging"""
        with self.assertLogs("log_event", level="WARNING") as log:
            log_event("test_user", "expired")
        self.assertIn("Login event - Username: test_user, Status: expired", log.output[0])

    def test_03_log_failed(self):
        """Positive test log_event failed status of logging"""
        with self.assertLogs("log_event", level="ERROR") as log:
            log_event("test_user", "failed")
        self.assertIn("Login event - Username: test_user, Status: failed", log.output[0])

    def test_04_log_unknown_status(self):
        """Negative test log_event unknown status of logging"""
        with self.assertLogs("log_event", level="ERROR") as log:
            log_event("test_user", "unknown")
        self.assertIn("Login event - Username: test_user, Status: unknown", log.output[0])
        with self.assertLogs("log_event", level="ERROR") as log:
            log_event("test_user", "")
        self.assertIn("Login event - Username: test_user, Status: ", log.output[0])
        with self.assertLogs("log_event", level="ERROR") as log:
            log_event("test_user", None)
        self.assertIn("Login event - Username: test_user, Status: None", log.output[0])

    def test_05_log_special_characters_username(self):
        """Negative test log_event special characters in username"""
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("user@123!", "success")
        self.assertIn("Login event - Username: user@123!, Status: success", log.output[0])

    def test_06_log_none_username(self):
        """Negative test log_event username is None"""
        with self.assertLogs("log_event", level="INFO") as log:
            log_event(None, "success")
        self.assertIn("Login event - Username: None, Status: success", log.output[0])

    def test_07_log_empty_username(self):
        """Negative test log_event with empty username"""
        with self.assertLogs("log_event", level="INFO") as log:
            log_event("", "success")
        self.assertIn("Login event - Username: , Status: success", log.output[0])

    def test_08_log_empty_username(self):
        """Negative test log_event with integer username"""
        with self.assertLogs("log_event", level="INFO") as log:
            log_event(123, "success")
        self.assertIn("Login event - Username: 123, Status: success", log.output[0])

    def test_09_levels(self):
        """Positive test of level of logging"""
        with self.assertNoLogs("log_event", level="CRITICAL") as log:
            log_event("test_user", "failed")
        with self.assertNoLogs("log_event", level="ERROR") as log:
            log_event("test_user", "expired")
        with self.assertNoLogs("log_event", level="WARNING") as log:
            log_event("test_user", "success")

if __name__ == "__main__":
    unittest.main(verbosity=2)
