#!/usr/bin/python3
"""
test differents behaviors of the Rectangle class
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import os

class TestCodeFormat(unittest.TestCase):
    def tester_pycodestyle(self):
        """Test that we conform to Pycodestyle (PEP-8)"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    
    def set_up(self):
        """Set to 0 the number of objects"""
        Base._Base__nb_objects = 0
    
    def tester_id_default(self):
        """Tester for positive Base Class id"""
        self.set_up()
        b1 = Rectangle(15, 4)
        b1.id = 1
        self.assertEqual(b1.id, 1)
        b2 = Rectangle(20, 8)
        b2.id = 2
        self.assertEqual(b2.id, 2)
    
    def test_instance_rectangle(self):
        """Tester if Rectangle is instance of Base"""
        r1 = Rectangle(42, 2, 32, 63, 27)
        self.assertEqual(type(r1), Rectangle)
        self.assertTrue(type(r1) == Rectangle)
        self.assertFalse(type(r1) == Base)
    
    def test_given(self):
        """Tester given id"""
        r4 = Rectangle(20, 55, 4, 66, 10)
        self.assertEqual(r4.id, 10)
    
    def tester_arguments_wrong(self):
        """Tester of wrong arguments"""
        with self.assertRaises(TypeError):
            r5 = Rectangle(20)
        with self.assertRaises(TypeError):
            r5 = Rectangle(52, 25, 33, 34, 22, 2)
    
class Tester_Rectangle_Attributes(unittest.TestCase):
    """Class to test attributes of Rectangle class"""
    def set_up(self):
        """Set to 0 the number of objects"""
        Base._Base__nb_objects = 0
    
    def tester_correct_sett_att(self):
        """Tester with the correct attributes"""
        r1 = Rectangle(20, 51, 3, 13, 22)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 51)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 13)
        self.assertEqual(r1.id, 22)
    
    def tester_parameters_greaterthan0(self):
        """Tester if width and height greather than 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(20, 4)
            r1.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(30, 5)
            r1.height = -14
    
    def tester_x_y_greater0(self):
        """Tester if x or y greater than 0"""
        self.set_up()
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(20, 32, 44, -6)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(40, 20, -6, -8)
    
    def tester_privates(self):
        """Tester the class if we try to do a private attribute"""
        self.set_up()
        r2 = Rectangle(20, 4, 10, 12)
        self.assertEqual(r2.x, 10)
        with self.assertRaises(AttributeError):
            r2.__x


class Tester_Rectangle_Area(unittest.TestCase):
    """This tester is tester to area of the Rectangle"""
    def set_up(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0
    
    def tester_area(self):
        self.set_up()
        b1 = Rectangle(20, 30)
        self.assertEqual(b1.area(), 600)
        b1.width = 50
        self.assertEqual(b1.area(), 1500)

    def tester_wrong(self):
        """Tester when a height is zero but this raises ValueError"""
        self.set_up()
        b2 = Rectangle(15, 2)
        self.assertEqual(b2.height, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            b2.height = 0


#Aqui me quede modificar de aca para abajo el contenido
#################################################

class Tester_display(unittest.TestCase):
    """Tester class display method"""
    def set_nb_to_zero(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_valid_attrs(self):
        """valid attrs for rectangle"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n\n  ##\n  ##\n  ##\n")
    
    def test_invalid_attrs(self):
        """Invalid attrs for rectangle"""
        self.set_nb_to_zero()
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 1, -2)
            r1.display()

    def test_call_display_with_args(self):
        """pass 1 arg to display"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        with self.assertRaises(TypeError):
            r1.display(1)

class Test_Update(unittest.TestCase):
    """Test class for update method"""
    def set_nb_to_zero(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_0_args(self):
        """pass no args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update()
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 10)

    def test_1_args(self):
        """pass 1 arg to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100)
        self.assertEqual(r1.id, 100)

    def test_2_args(self):
        """pass 2 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)

    def test_3_args(self):
        """pass 3 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)

    def test_4_args(self):
        """pass 4 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)

    def test_5_args(self):
        """pass 5 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400, 500)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)
        self.assertEqual(r1.y, 500)

    def test_more_than_5_args(self):
        """pass more of 5 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(100, 200, 300, 400, 500, 600, 700, 800)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 300)
        self.assertEqual(r1.x, 400)
        self.assertEqual(r1.y, 500)

    def test_id_kwargs(self):
        """pass id kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123)
        self.assertEqual(r1.id, 123)

    def test_width_kwargs(self):
        """pass id width kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)

    def test_height_kwargs(self):
        """pass if widt height kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)

    def test_x_kwargs(self):
        """pass if widt height x kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432, x=940)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)
        self.assertEqual(r1.x, 940)

    def test_y_kwargs(self):
        """pass if widt height x y kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432, x=940, y=758)
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)
        self.assertEqual(r1.x, 940)
        self.assertEqual(r1.y, 758)

    def test_more_kwargs(self):
        """pass valid and not valid kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(id=123, width=987, height=432, x=940, y=758, other='random')
        self.assertEqual(r1.id, 123)
        self.assertEqual(r1.width, 987)
        self.assertEqual(r1.height, 432)
        self.assertEqual(r1.x, 940)
        self.assertEqual(r1.y, 758)
        string = "'Rectangle' object has no attribute 'other'"
        with self.assertRaisesRegex(AttributeError, string):
            self.assertEqual(r1.other, 'random')

    def test_args_and_kwargs(self):
        """pass args and kwargs to function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        r1.update(129, 234, id=123, width=987, height=432, x=940, y=758,
                  other='random')
        self.assertEqual(r1.id, 129)
        self.assertEqual(r1.width, 234)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 0)
        string3 = "'Rectangle' object has no attribute 'other'"
        with self.assertRaisesRegex(AttributeError, string3):
            self.assertEqual(r1.other, 'random')

    def test_1_args_invalid(self):
        """pass 1 invalid arg to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)

        # pass negative int
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1.update(100, -23)

        # pass str
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1.update(321, 'randval')
        
        # pass float to update height
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r1.update(28, 3, 23.43, 342)
    
    def test_args_as_iterable_obj(self):
        """pass iterable args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)

        # pass list to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = [1, 2, 3]
            r1.update(2, ls)

        # pass tuple to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = (1, 2, 3)
            r1.update(2, ls)

        # pass set to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = {1, 2, 3}
            r1.update(2, ls)

        # pass dict to update
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            ls = {'width': 1, 'x': 2, 'y': 3}
            r1.update(2, ls)

    def test_args_invalid(self):
        """pass 2 args to update function"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r1.update(100, 200, -43)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r1.update(100, 200, 903, 23, -43)

        # invalid last arg passes because is not taken into account
        r1.update(100, 200, 903, 23, 345, 49, -43)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 903)
        self.assertEqual(r1.x, 23)
        self.assertEqual(r1.y, 345)

class Test_Dictionary_Representation(unittest.TestCase):
    """Test case class for update function"""
    def set_nb_to_zero(self):
        """set to 0 the number of objects"""
        Base._Base__nb_objects = 0

    def test_pass_1_arg(self):
        """pass one argument to function call"""
        self.set_nb_to_zero()
        r1 = Rectangle(2, 1, 10, 0, 1)
        self.assertEqual(r1.id, 1)
        string10 = "takes 1 positional argument but 2 were given"
        with self.assertRaisesRegex(TypeError, string10):
            r1.to_dictionary(239)

    def test_ret_dict(self):
        """Test to dictionary function"""
        r1 = Rectangle(23, 43, 129, 32, 2)
        self.assertEqual(2, r1.id)
        d_comp = {'id': 2, 'width': 23, 'height': 43, 'x': 129, 'y': 32}
        self.assertDictEqual(r1.to_dictionary(), d_comp)

    def test_dict_with_args(self):
        """Test to dictionary function"""
        r1 = Rectangle(10, 2, 1, 9, 9)
        r1_dict = r1.to_dictionary()
        d = {'x': 1, 'y': 9, 'id': 9, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dict, d)

        self.assertEqual(type(r1_dict), dict)

        r2 = Rectangle(10, 2, 1, 9, 10)
        r2_dict = r2.to_dictionary()
        d = {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10}
        self.assertDictEqual(r2_dict, d)

        self.assertEqual(r1 == r2, False)
    
class TestRectangle(unittest.TestCase):
    """Test the functionality of the rectangle class"""

    @classmethod
    def setUpClass(cls):
        """"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
    
    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_str(self):
        """Test the str method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")

        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")

        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")

        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")