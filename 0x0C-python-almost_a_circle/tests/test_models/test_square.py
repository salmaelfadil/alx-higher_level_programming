#!/usr/bin/python3
"""test module for square class"""
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest
from io import StringIO
import sys
from unittest.mock import patch

class TestSquare(unittest.TestCase):
    """unit test for square"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_squares(self):
        """Test new squares"""
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_create_instance(self):
        """Test creating an instance of Square"""
        instance = Square(5)
        self.assertIsInstance(instance, Square)

    def test_size_property(self):
        """Test the size property of Square"""
        instance = Square(5)
        self.assertEqual(instance.size, 5)

    def test_size_setter(self):
        """Test the size setter of Square"""
        instance = Square(5)
        instance.size = 10
        self.assertEqual(instance.size, 10)
        self.assertEqual(instance.width, 10)
        self.assertEqual(instance.height, 10)

    def test_update(self):
        """ Test update method """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method of Square"""
        instance = Square(5, id=1, x=2, y=3)
        dictionary = instance.to_dictionary()
        self.assertEqual(dictionary, {'id': 1, 'size': 5, 'x': 2, 'y': 3})

    def test_display(self):
        """ Test string printed """
        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)
    
    def test_load_from_file(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
