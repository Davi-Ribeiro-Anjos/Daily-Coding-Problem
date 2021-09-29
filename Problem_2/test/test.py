import unittest

from Problem_2.main import problem


class ListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.exemple_1 = [1, 2, 3, 4, 5]
        self.exemple_2 = [3, 2, 1]

        self.list_1 = [1, 3, 5, 2, 10]
        self.list_2 = [1, 2, 2, 5, 8]
        self.list_3 = [5, 6, 6, 5]

    def test_verify_if_is_equal_problem(self):
        self.assertEqual(problem(self.exemple_1), [120, 60, 40, 30, 24])
        self.assertEqual(problem(self.exemple_2), [2, 3, 6])
    
    def test_verify_if_is_equal_custom(self):
        self.assertEqual(problem(self.list_1), [300, 100, 60, 150, 30])
        self.assertEqual(problem(self.list_2), [160, 80, 80, 32, 20])
        self.assertEqual(problem(self.list_3), [180, 150, 150, 180])