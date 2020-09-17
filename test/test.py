import unittest
from src.vector import Vector


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        _sum = self.v1 + self.v2
        self.assertEqual(getattr(_sum, 'x'), 4.0)
        self.assertEqual(getattr(_sum, 'y'), 4.0)
        self.assertEqual(getattr(_sum, 'z'), 7.0)

    def test_subtraction(self):
        _diff = self.v1 - self.v2
        self.assertEqual(getattr(_diff, 'x'), -2.0)
        self.assertEqual(getattr(_diff, 'y'), -8.0)
        self.assertEqual(getattr(_diff, 'z'), -11.0)

    def test_multiplication(self):
        _mul = self.v1 * 2
        self.assertEqual(getattr(_mul, 'x'), 2.0)
        self.assertEqual(getattr(_mul, 'y'), -4.0)
        self.assertEqual(getattr(_mul, 'z'), -4.0)

    def test_division(self):
        _div = self.v1 / self.v2
        self.assertEqual(getattr(_div, 'x'), 2.0)
        self.assertEqual(getattr(_div, 'y'), -4.0)
        self.assertEqual(getattr(_div, 'z'), -4.0)


if __name__ == '__main__':
    unittest.main()
