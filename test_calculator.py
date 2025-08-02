# https://github.com/RakiClaymore/lab10-CC-AK
# Partner 1: Chloe Coile
# Partner 2: Amphitreatte Kreiman

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
        # Partner 2

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-3, -1), -2)
        self.assertEqual(subtract(0, 3), -3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
    #     fill in code
        expected = 20
        result = mul(10, 2)
        self.assertEqual(result, expected)


    def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
        expected = 1.5
        result = div(2,3)
        self.assertEqual(result, expected)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(5, 25), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 8)


    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        expected = 5.0
        result = hypotenuse(3, 4)
        self.assertEqual(result, expected)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
        with self.assertRaises(ValueError):
            square_root(-3)

        expected = 2
        result = square_root(4)
        self.assertEqual(result, expected)

# Do not touch this
if __name__ == "__main__":
    unittest.main()