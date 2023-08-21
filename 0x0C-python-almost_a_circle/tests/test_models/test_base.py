#!/usr/bin/python3
"""test Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseMethods(unittest.TestCase):
    """test base class"""

    def test_id(self):
        """test id"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_repeated_it(self):
        """test repeated ids"""
        b1 = Base()
        b2 = Base()
        b3 = Base(2)
        b4 = Base(5)
        b5 = base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 5)
        self.asserEqual(b5.id, 3)

    def test_string_id(self):
        """test string id"""
        b = Base('2')
        self.assertEqual(b.id, '2')

    def test_more_args(self):
        """test passing more than one argument to init"""
        with self.assertRaises(TypeError):
            b = Base(2, 2)
    
    def test_access_private_attr(self):
        """test accessing private attributes"""
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects
