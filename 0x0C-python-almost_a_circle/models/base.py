#!/usr/bin/python3
"""Definition class"""
import json
import os
import turtle
import csv


class Base:
    """Definition Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This class will be the “base” of all other
        classes in this project"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""

        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        result = []
        namefile = cls.__name__ + ".json"
        options = ["Rectangle", "Square"]
        name = ""

        if (list_objs is not None and len(list_objs)):
            name = type(list_objs[0]).__name__
            if (name in options):
                if all((type(obj).__name__ == name) for obj in list_objs):
                    result = [obj.to_dictionary() for obj in list_objs]

        with open(namefile, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""
        list_new = []

        if ((json_string is not None) or (len(json_string) != 0)):
            list_new = json.loads(json_string)

        return (list_new)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        - Create a Rectangle or Square instance with “dummy”
        mandatory attributes (width, height, size, etc.)
        - Call update instance method to this “dummy” instance
        to apply your real values
        """
        if (cls.__name__) == "Rectangle":
            dummy = cls(2, 2)
        if (cls.__name__) == "Square":
            dummy = cls(2)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances:
        - The filename must be: <Class name>.json
        - If the file doesn’t exist, return an empty list
        - Otherwise, return a list of instances - the type of these instances
        depends on cls (current class using this method)
        """
        filename = cls.__name__ + ".json"
        json_string = ""
        devolution = []

        if os.path.exists('./{:s}'.format(filename)):
            with open(filename, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                list_instances = cls.from_json_string(json_string)
                for dic in list_instances:
                    devolution.append(cls.create(**dic))

        return devolution

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialization to file csv"""
        result = "[]"
        filename = cls.__name__ + ".csv"
        options = ["Rectangle", "Square"]
        name = ""

        if (list_objs is not None and len(list_objs)):
            name = type(list_objs[0]).__name__
            if (name in options):
                if all((type(obj).__name__ == name) for obj in list_objs):
                    result = [list(obj.to_dictionary().values())
                              for obj in list_objs]

        with open(filename, mode="w", encoding="utf-8") as f:
            for data in result:
                f.write(",".join(str(data)[1:-1].split(", ")) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Read a CSV file and create instances from the dicts"""

        filename = cls.__name__ + ".csv"
        option_rec = ["id", "width", "height", "x", "y"]
        option_sq = ["id", "size", "x", "y"]
        result = []

        if os.path.exists("./{:s}".format(filename)):
            with open(filename, mode="r", encoding="utf-8") as f:
                data_csv = csv.reader(f)
                if (cls.__name__ == "Rectangle"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(option_rec, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))
                elif (cls.__name__ == "Square"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(option_sq, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))
        return (result)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        """
        turtle.shape("turtle")
        for rectangle in list_rectangles:
            turtle.goto(rectangle.x, rectangle.y)
            for i in range(4):
                turtle.pendown()
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.penup()
        for square in list_squares:
            turtle.goto(square.x, square.y)
            for i in range(4):
                turtle.pendown()
                turtle.forward(square.size)
                turtle.right(90)
                turtle.penup()

        turtle.done()
