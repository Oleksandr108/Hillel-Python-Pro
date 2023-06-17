import unittest
from unittest.mock import patch
from unittest import TestCase
from drunk_polish_calculator import op_plus, op_minus, op_multiply, op_divide, main

class Drunk_TestCase(TestCase):
    def test_op_plus(self):
        self.assertEqual(op_plus(8, 5), 13.0)
        self.assertEqual(op_plus(-20, 5), -15.0)
        self.assertEqual(op_plus(0, 0), 0)

    def test_op_minus(self):
        self.assertEqual(op_minus(5, 2), -3.0)
        self.assertEqual(op_minus(-10, 5), 15.0)
        self.assertEqual(op_minus(0, 0), 0)

    def test_op_multiply(self):
        self.assertEqual(op_multiply(7, 4), 28.0)
        self.assertEqual(op_multiply(-2, 5), -10.0)
        self.assertEqual(op_multiply(0, 10), 0)

    def test_op_divide(self):
        self.assertEqual(op_divide(-6, -3), 2.0)
        self.assertEqual(op_divide(10, -5), -2,0)
        self.assertEqual(op_divide(12, 4), 3.0)

    @patch('builtins.input', return_value='3 4 *')
    def test_main(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with(12.0)

if __name__ == '__main__':
    unittest.main()

