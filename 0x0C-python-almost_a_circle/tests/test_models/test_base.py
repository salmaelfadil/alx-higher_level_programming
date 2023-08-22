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
        b1 = Base(1)
        b2 = Base()
        b3 = Base(2)
        b4 = Base(5)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 5)
        self.assertEqual(b5.id, 3)

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

    def test_to_json_string(self):
        """Test converting a list of dictionaries to JSON string"""
        dictionary_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(dictionary_list)
        self.assertEqual(json_string, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_from_json_string(self):
        """Test converting a JSON string to a list of dictionaries"""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        dictionary_list = Base.from_json_string(json_string)
        self.assertEqual(len(dictionary_list), 2)
        self.assertEqual(dictionary_list[0]['name'], 'Alice')
        self.assertEqual(dictionary_list[1]['name'], 'Bob')

