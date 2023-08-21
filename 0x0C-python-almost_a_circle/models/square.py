#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inhertis from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initalizes instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size method"""
        self.width = value
        self.height = value

    def __str__(self):
        """overrides the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
