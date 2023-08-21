#!/usr/bin/python3
"""unit test for rectangle model"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unit test for rectangle class"""

    def setUp(self):
        """set up for each test"""
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """test new rectangle"""
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_None_width(self):
        """test with no width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """test with string width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_new_rectangle_2(self):
        """test new rectangle with all attrs"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_is_Base_instance(self):
        """test rectnagle is instance of base"""
        r = Rectangle(1, 1)
        self.assertEqual(True, isinstance(r, Base))

    def test_incorrect_amount_attrs(self):
        """test with 0 args passed"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_area(self):
        """area test """
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
