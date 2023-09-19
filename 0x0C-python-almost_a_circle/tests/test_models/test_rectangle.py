#!/usr/bin/python3
"""unit test for rectangle model"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


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

    def test_width_property(self):
        """Test the width property of Rectangle"""
        instance = Rectangle(5, 10)
        self.assertEqual(instance.width, 5)

    def test_height_property(self):
        """Test the height property of Rectangle"""
        instance = Rectangle(5, 10)
        self.assertEqual(instance.height, 10)

    def test_width_setter(self):
        """Test the width setter of Rectangle"""
        instance = Rectangle(5, 10)
        instance.width = 20
        self.assertEqual(instance.width, 20)

    def test_height_setter(self):
        """Test the height setter of Rectangle"""
        instance = Rectangle(5, 10)
        instance.height = 15
        self.assertEqual(instance.height, 15)

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
    
    def test_to_dictionary_method(self):
        """Test the to_dictionary method of Rectangle"""
        instance = Rectangle(5, 10, id=1, x=2, y=3)
        dictionary = instance.to_dictionary()
        self.assertEqual(dictionary, {id: 1, width: 5, height: 10, x: 2, y: 3})

    def test_display_method(self):
        """Test the display method of Rectangle"""
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method of Rectangle"""
        instance = Rectangle(5, 10, id=1, x=2, y=3)
        dictionary = instance.to_dictionary()
        self.assertEqual(dictionary, {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3})

    def test_dict_to_json(self):
        """Test dictrionary to JSON string"""
        new = Rectangle(2, 2)
        dictionary = new.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

