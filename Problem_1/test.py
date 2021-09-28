import unittest

from .main import Problem

class ListTestCase(unittest.TestCase):
    def setUp(self):
        self.list_1 = [1, 4, 10, 5, 27, 50, 13, 8, 2]
        self.list_2 = [2, 89, 12, 46, 10, 3, 23, 9, 7, 15]
    
    def test_verify_if_is_true(self):
        self.assertTrue(Problem(self.list_1, 15))
        self.assertTrue(Problem(self.list_2, 92))
    
    def test_verify_if_is_false(self):
        self.assertFalse(Problem(self.list_1, 16))
        self.assertFalse(Problem(self.list_2, 20))
