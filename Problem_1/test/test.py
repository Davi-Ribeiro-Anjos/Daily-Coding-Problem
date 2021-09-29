import unittest

from Problem_1.main import problem


class ListTest(unittest.TestCase):
    def setUp(self):
        self.example = [10, 15, 3, 7]

        self.list_1 = [1, 4, 10, 5, 27, 50, 13, 8, 2]
        self.list_2 = [2, 89, 12, 46, 10, 3, 23, 9, 7, 15]
    

    def test_verify_if_is_true_example(self):
        self.assertTrue(problem(self.example, 17))

    def test_verify_if_is_false_example(self):
        self.assertFalse(problem(self.example, 19))


    def test_verify_if_is_true_custom(self):
        self.assertTrue(problem(self.list_1, 15))
        self.assertTrue(problem(self.list_2, 92))
    
    def test_verify_if_is_false_custom(self):
        self.assertFalse(problem(self.list_1, 16))
        self.assertFalse(problem(self.list_2, 20))
