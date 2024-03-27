# unit_test.py
import unittest
from calculator import Calculator
import json

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        print("1.Test : Toplama Testi : Başarılı")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        print("2.Test : Çıkarma Testi : Başarılı")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        print("3.Test : Çarpma Testi : Başarılı")

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        print("4.Test : Bölme Testi : Başarılı")

if __name__ == '__main__':
    unittest.main()




