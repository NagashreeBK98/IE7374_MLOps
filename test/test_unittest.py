import unittest
from src.calculator import fun1, fun2, fun3, fun4

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(10, 5), 15)

    def test_fun2(self):
        self.assertEqual(fun2(10, 5), 5)

    def test_fun3(self):
        self.assertEqual(fun3(3, 4), 12)

    def test_fun4(self):
        self.assertEqual(fun4(2, 3), 10)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fun2("x", 3)

if __name__ == "__main__":
    unittest.main()
