import unittest
from unittest.mock import patch, MagicMock

from homework11 import log_event  # импорт функции из homework11.py

class TestLogEvent(unittest.TestCase):

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_success_log(self, mock_basicConfig, mock_getLogger):
        mock_logger = MagicMock()
        mock_getLogger.return_value = mock_logger
        log_event('testuser', 'success')
        mock_logger.info.assert_called_once_with('Login event - Username: testuser, Status: success')
        mock_logger.warning.assert_not_called()
        mock_logger.error.assert_not_called()

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_expired_log(self, mock_basicConfig, mock_getLogger):
        mock_logger = MagicMock()
        mock_getLogger.return_value = mock_logger
        log_event('testuser', 'expired')
        mock_logger.warning.assert_called_once_with('Login event - Username: testuser, Status: expired')
        mock_logger.info.assert_not_called()
        mock_logger.error.assert_not_called()

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_failed_log(self, mock_basicConfig, mock_getLogger):
        mock_logger = MagicMock()
        mock_getLogger.return_value = mock_logger
        log_event('testuser', 'failed')
        mock_logger.error.assert_called_once_with('Login event - Username: testuser, Status: failed')
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

    @patch('logging.getLogger')
    @patch('logging.basicConfig')
    def test_unknown_status_log(self, mock_basicConfig, mock_getLogger):
        mock_logger = MagicMock()
        mock_getLogger.return_value = mock_logger
        log_event('testuser', 'unknown')
        mock_logger.error.assert_called_once_with('Login event - Username: testuser, Status: unknown')
        mock_logger.info.assert_not_called()
        mock_logger.warning.assert_not_called()

if __name__ == '__main__':
    unittest.main()
