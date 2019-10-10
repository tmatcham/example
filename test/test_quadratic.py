import unittest
from quadratic import quadratic_solver

class test_quadratic(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(quadratic_solver(1, 2, 1), [-1])

    def test_2(self):
        self.assertIn(1, quadratic_solver(-1, 0, 1))
        self.assertIn(-1, quadratic_solver(-1, 0, 1))
        self.assertEqual(len(quadratic_solver(-1, 0, 1)), 2)

    def test_4(self):
        with self.assertRaises(ValueError):
            quadratic_solver(0, 0, 1)