import unittest
from homework_11 import log_event

# Helper Function to Get Log Message from File

def get_last_log_message(log_filename='login_system.log'):
    """Helper function to get the last log message from the log file."""
    with open(log_filename, 'r') as log_file:
        log_contents = log_file.readlines()
    return log_contents[-1] if log_contents else None

class LogEventTest(unittest.TestCase):

    def test_01_log_event(self):
        """Check if message is logged on 'info' level"""
        username = "ilazurkevych"
        status = "success"
        log_event(username, status)
        actual_last_log = get_last_log_message()
        actual = actual_last_log.split(' - ', 1)[-1].strip()
        expected = f"Login event - Username: {username}, Status: success"
        self.assertEqual(actual, expected, msg = "Message is NOT logged on 'info' level.")

    def test_02_log_event(self):
        """Check if message is logged on 'warning' level"""
        username = "ilazurkevych"
        status = "expired"
        log_event(username, status)
        actual_last_log = get_last_log_message()
        actual = actual_last_log.split(' - ', 1)[-1].strip()
        expected = f"Login event - Username: {username}, Status: expired"
        self.assertEqual(actual, expected, msg = "Message is NOT logged on 'warning' level.")

    def test_03_log_event(self):
        """Check if message is logged on 'error' level."""
        username = "ilazurkevych"
        status = "failed"
        log_event(username, status)
        actual_last_log = get_last_log_message()
        actual = actual_last_log.split(' - ', 1)[-1].strip()
        expected = f"Login event - Username: {username}, Status: failed"
        self.assertEqual(actual, expected, msg = "Message is NOT logged on 'error' level.")

    def test_04_log_event(self):
        """Check if ValueError is raised for any other status that differs from 'success', 'expired', 'failed'."""
        username = "ilazurkevych"
        status = "debug"
        log_event(username, status)
        actual_last_log = get_last_log_message()
        actual = actual_last_log.split(' - ', 1)[-1].strip()
        expected = f"Login event - Username: {username}, Status: debug"
        self.assertNotEqual(actual, expected, msg = f"Error: Message log is not expected for any other statuses that differs from 'success', 'expired', 'failed'.")

    def test_05_log_event(self):
        """Check if log message contains a timestamp."""
        username = "ilazurkevych"
        status = "success"
        log_event(username, status)
        actual_last_log = get_last_log_message()
        actual = actual_last_log.startswith("2025")
        self.assertTrue(actual, msg = "Error: Timestamp is missing or incorrect.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
