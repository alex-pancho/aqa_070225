import unittest
from unittest.mock import patch
from homework_11 import log_event  

class TestLogEvent(unittest.TestCase):
    
    @patch("homework_11.logging.getLogger")
    def test_log_success(self, mock_logger):
        # Verify that the logger records a successful login event.
        log_event("user1", "success")
        mock_logger.return_value.info.assert_called_with("Login event - Username: user1, Status: success")

    @patch("homework_11.logging.getLogger")
    def test_log_expired(self, mock_logger):
        # Verify that the logger records a warning for an expired password.
        log_event("user2", "expired")
        mock_logger.return_value.warning.assert_called_with("Login event - Username: user2, Status: expired")

    @patch("homework_11.logging.getLogger")
    def test_log_failed(self, mock_logger):
        # Verify that the logger records an error for a failed login attempt.
        log_event("user3", "failed")
        mock_logger.return_value.error.assert_called_with("Login event - Username: user3, Status: failed")
    
    @patch("homework_11.logging.getLogger")
    def test_invalid_status(self, mock_logger):
        # Checking that the function logs an error for an unsupported status
        log_event("user5", "unknown_status")
        mock_logger.return_value.error.assert_called_with("Login event - Username: user5, Status: unknown_status")

    @patch("homework_11.logging.getLogger")
    def test_empty_username(self, mock_logger):
        # Verify that the logger records an event even with an empty username.
        log_event("", "success")
        mock_logger.return_value.info.assert_called_with("Login event - Username: , Status: success")
    

    @patch("homework_11.logging.getLogger")
    def test_empty_status(self, mock_logger):
        # Verify that the logger records an error when the status is empty.
        log_event("user4", "")
        mock_logger.return_value.error.assert_called_with("Login event - Username: user4, Status: ")

    @patch("homework_11.logging.getLogger")
    def test_empty_username_and_status(self, mock_logger):
        # Checking that empty values for username and status are handled properly.
        log_event("", "")
        mock_logger.return_value.error.assert_called_with("Login event - Username: , Status: ")
    
    @patch("homework_11.logging.getLogger")
    def test_multiple_log_events(self, mock_logger):
        # Сhecking few calls in a raw
        log_event("user8", "success")
        log_event("user9", "failed")
        mock_logger.return_value.info.assert_called_with("Login event - Username: user8, Status: success")
        mock_logger.return_value.error.assert_called_with("Login event - Username: user9, Status: failed")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
        

              



