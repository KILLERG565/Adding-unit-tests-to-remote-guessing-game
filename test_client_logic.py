import unittest
from unittest.mock import MagicMock
from client_logic import receive_data, send_data, is_correct_reply

class TestClientLogic(unittest.TestCase):

    def test_receive_data(self):
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b"Hello\n"
        self.assertEqual(receive_data(mock_socket), "Hello")

    def test_send_data(self):
        mock_socket = MagicMock()
        send_data(mock_socket, "Hello")
        mock_socket.sendall.assert_called_with(b"Hello")

    def test_is_correct_reply(self):
        self.assertTrue(is_correct_reply("CORRECT!"))
        self.assertFalse(is_correct_reply("Try again"))

if __name__ == '__main__':
    unittest.main()
