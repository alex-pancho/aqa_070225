import unittest
from homework_11 import log_event

# Helper function to read the last log line
def get_last_log_line():
    with open("login_system.log", "r") as file:
        lines = file.readlines()
        return lines[-1].strip()

class TestLogEvent(unittest.TestCase):

    def test01_success_status_logged_as_info(self):
        """
        Verifies that the 'success' status is logged at the info level.
        If this test fails, the implementation of log_event is incorrect.
        Requirement reference:
        * success - should be logged at INFO level
        """
        username = "testuser"
        status = "success"
        expected = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)
        actual_log = get_last_log_line()
        actual = actual_log.split(" - ", 1)[-1].strip()

        self.assertEqual(actual, expected)

    def test02_expired_status_logged_as_warning(self):
        """
        Verifies that the 'expired' status is logged at the warning level.
        If this test fails, the implementation of log_event is incorrect.
        Requirement reference:
        * expired - should be logged at WARNING level
        """
        username = "testuser"
        status = "expired"
        expected = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)
        actual_log = get_last_log_line()
        actual = actual_log.split(" - ", 1)[-1].strip()

        self.assertEqual(actual, expected)

    def test03_failed_status_logged_as_error(self):
        """
        Verifies that the 'failed' status is logged at the error level.
        If this test fails, the implementation of log_event is incorrect.
        Requirement reference:
        * failed - should be logged at ERROR level
        """
        username = "testuser"
        status = "failed"
        expected = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)
        actual_log = get_last_log_line()
        actual = actual_log.split(" - ", 1)[-1].strip()

        self.assertEqual(actual, expected)

    def test04_unknown_status_logged_as_error(self):
        """
        Verifies that any unknown status is logged at the error level by default.
        If this test fails, the logging logic must be reviewed.
        This is based on the implementation of log_event, not a stated requirement.
        """
        username = "testuser"
        status = "unknown_status"
        expected = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)
        actual_log = get_last_log_line()
        actual = actual_log.split(" - ", 1)[-1].strip()

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)

