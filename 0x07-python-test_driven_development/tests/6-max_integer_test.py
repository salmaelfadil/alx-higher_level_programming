#!/usr/bin/python3

import unittest

def max_integer(list=[]):
    """function that returns tha maximum integer in the list"""
    if not list:
        return None
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

"""Unittest for max_integer"""
class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Tests for empty list []"""
        l = []
        self.assertIsNone(max_integer(l))
    
    def test_no_args(self):
        """Test for no arguments"""
        self.assertIsNone(max_integer())

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        o = [1, 2, 3, 4]
        self.assertEqual(max_integer(o), 4)
    
    def test_unordered_list(self):
        """Test an unordered list"""
        unordered = [3, 1, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_negative(self):
        """Test list with negative numbers"""
        n = [-1, -50, -25, -2, -6]
        self.assertEqual(max_integer(n), -1)

    def test_one_element(self):
        """Test for one number in list"""
        l = [1]
        self.assertEqual(max_integer(l), 1)

if __name__ == "__main__":
    unittest.main()
