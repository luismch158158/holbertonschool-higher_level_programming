#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Class of unittest of max integer function"""

    def documentation_tester(self):

        """Unittesting if function have a documentation"""

        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.my_function.__doc__) > 0)

    def tester_positives(self):
        """In this unittest only positive number will be tested"""

        self.assertEqual(max_integer([1, 2, 3]), 3)

        self.assertEqual(max_integer([42, 55, 66, 85]), 85)

        self.assertEqual(max_integer([50, 1, 5, 10]), 50)

        self.assertEqual(max_integer([44, 34, 22, 11]), 44)

        self.assertEqual(max_integer([55, 15, 2, 5]), 55)

        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

        self.assertEqual(max_integer([22, 1]), 22)

        self.assertEqual(max_integer([5, 12, 2]), 12)

        self.assertEqual(max_integer([5]), 5)

        self.assertEqual(max_integer([150, 500, 200, 1000, 520]), 1000)

        self.assertEqual(max_integer([54, 53, 66]), 66)

    def tester_boolean(self):
        """Tester of boolean"""
        self.assertEqual(max_integer([True, False, True]), True)

    def tester_data_mix(self):
        """In this unittest data mixed numbers will be tested"""

        self.assertEqual(max_integer([-5, -40, 4, -1]), 4)

        self.assertEqual(max_integer([-2, -80, -4, 10]), 10)

        self.assertEqual(max_integer([-50, -50, -50, 1]), 1)

        self.assertEqual(max_integer([-1, -2, -3, 2]), 2)

        self.assertEqual(max_integer([-80, 4, -45, 5]), 5)

        self.assertEqual(max_integer([-99, -100, 100, -44]), 100)

        self.assertEqual(max_integer([100, 200, 3, -500]), 200)

        self.assertEqual(max_integer([44, -50, -100, 1]), 44)

        self.assertEqual(max_integer([50, 40, -44, 11]), 50)

    def tester_negatives(self):
        """In this unittest only negative numbers will be tested"""

        self.assertEqual(max_integer([-5, -4, -3, -2]), -2)

        self.assertEqual(max_integer([-42, -55, -66, -85]), -42)

        self.assertEqual(max_integer([-6, -15, -100, -12]), -6)

        self.assertEqual(max_integer([-2, -200, -2000, -20000]), -2)

        self.assertEqual(max_integer([-5, -4]), -4)

        self.assertEqual(max_integer([-500, -1]), -1)

        self.assertEqual(max_integer([-2, -55, -44, -1]), -1)

        self.assertEqual(max_integer([-51, -4, -66, -4]), -4)

    #def tester_not_is_list(self):
        #"""In this unittest only incorrect data types will be tested"""

        #"""Also make sure value errors are raised when necessary"""

        #list_for_test = []
        #self.assertIsNone(max_integer(list_for_test))

        #list_for_test = []
        #self.assertEqual(max_integer(list_for_test), None)

        #list_for_test = [54, -55, "Hola", 4]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = [[54, -55], 40, 4]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = ["Como", "Estas", "?"]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = [1 + 50, ["hola", "como"], 4]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = ["54", "-55", "Hola", "4"]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = [0, 55.55, "Hola", 4]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = "Hola, como estas"
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = {12, True, -5, False}
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = {2, 55, 65, 5}
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = ["Hola?", -500.55]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = [55.44]
        #self.assertRaises(TypeError, max_integer, list_for_test)

        #list_for_test = ["Hello", -44.2, 52]
        #self.assertRaises(TypeError, max_integer, list_for_test)


if __name__ == "__main__":
    unittest.main()
