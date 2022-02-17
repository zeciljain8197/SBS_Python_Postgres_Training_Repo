import unittest
from calc import Calculator

o1 = Calculator()

class Test_Calc(unittest.TestCase):
    def test_add(self):
        res = o1.add(4, 5)
        self.assertEqual(res, 9)

    def test_sub(self):
        res = o1.sub(-5, -7)
        self.assertEqual(res, 2)

    def test_mul(self):
        res = o1.mul(4, -5)
        self.assertEqual(res, -20)

    def test_div(self):
        res = o1.div(0, 9)
        self.assertEqual(res, 0)

    def test_mod(self):
        res = o1.mod(8.2, 4.1)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
