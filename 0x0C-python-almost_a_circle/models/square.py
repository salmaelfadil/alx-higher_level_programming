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
        return "[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates attributes"""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary with attributes of square"""
        attrs = ['id', 'size', 'x', 'y']
        sq_dict = {}
        
        for attr in attrs:
            if attr == 'size':
                sq_dict[attr] = getattr(self, 'width')
            else:
                sq_dict[attr] = getattr(self, attr)
        return sq_dict
