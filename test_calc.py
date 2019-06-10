import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEquals(calc.add(4, 7), 11)

    def test_substract(self):
        self.assertEquals(calc.substract(12, 6), 6)


if __name__ == '__main__':
    unittest.main()
