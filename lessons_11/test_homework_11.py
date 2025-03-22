import unittest
from unittest.mock import patch
from homework_11 import log_event 


class TestLogging(unittest.TestCase):
    @patch("homework_11.logging.getLogger")
    def test_log_event_success(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("test_user", "success")
        mock_logger.info.assert_called_with("Login event - Username: test_user, Status: success")

    @patch("homework_11.logging.getLogger")
    def test_log_event_expired(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("test_user", "expired")
        mock_logger.warning.assert_called_with("Login event - Username: test_user, Status: expired")

    @patch("homework_11.logging.getLogger")
    def test_log_event_failed(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("test_user", "failed")
        mock_logger.error.assert_called_with("Login event - Username: test_user, Status: failed")

    @patch("homework_11.logging.getLogger")
    def test_log_event_unknown(self, mock_get_logger):
        mock_logger = mock_get_logger.return_value
        log_event("test_user", "unknown_status")
        mock_logger.error.assert_called_with("Login event - Username: test_user, Status: unknown_status")


if __name__ == "__main__":
    unittest.main(verbosity=2)

