#!/usr/bin/python3
"""
Unittest of the Base Class
"""
import unittest
import os
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    """
    Class of unittest to test Base Class
    """
    def tester_pycodestyle_base(self):
        """
        Test that checks Pycodestyle (PEP8)
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )
    
    def tester_of_id_positive(self):
        """
        Tester of positive id's
        """
        b1 = Base(150)
        self.assertEqual(b1.id, 150)
        b2 = Base(200)
        self.assertEqual(b2.id, 200)
        b3 = Base(300)
        self.assertEqual(b3.id, 300)
    
    def tester_of_id_null(self):
        """
        Tester of None id's
        """
        # b1 = Base()
        # self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def tester_of_id_negative(self):
        """
        Tester of negative id's
        """
        b1 = Base(-20)
        self.assertEqual(b1.id, -20)
        b2 = Base(-40)
        self.assertEqual(b2.id, -40)
        b3 = Base(-60)
        self.assertEqual(b3.id, -60)

    def tester_id_string(self):
        """
        Tester of id's string
        """
        b1 = Base("Hello People")
        self.assertEqual(b1.id, "Hello People")
        b2 = Base("Holberton")
        self.assertEqual(b2.id, "Holberton")
        b3 = Base("Luis")
        self.assertEqual(b3.id, "Luis")
        b4 = Base("Fernando")
        self.assertEqual(b4.id, "Fernando")

    def tester_to_json_string(self):
        """
        Tester of to_json_string method
        """
        b1 = Rectangle(10, 22, 62, 8)
        dictionary = b1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def tester_to_json_string_empty(self):
        """
        Tester to json_string empty
        """
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        data_none = None
        json_dictionary_2 = Base.to_json_string(data_none)
        self.assertEqual(json_dictionary_2, "[]")
    
    def tester_instance(self):
        """
        Tester instance of Base Class
        """
        p1 = Base()
        self.assertEqual(type(p1), Base)
        self.assertTrue(isinstance(p1, Base))

    def tester_to_json_string_dict(self):
        """
        Test functionality of json string
        """
        dictionary = {'id': 42, 'x': 55, 'y': 40, 'width': 52, 'height': 56}
        json_data = Base.to_json_string([dictionary])

        self.assertTrue(isinstance(dictionary, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 42, "x": 55, "y": 40, "width": 52, "height": 56]}'
        )
    
    def tester_to_json_string_wrong(self):
        """
        Tester of wrong functionality of this method
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_create(self):
        """
        Test create method
        """
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Monty Python')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(msg.exception)
        )