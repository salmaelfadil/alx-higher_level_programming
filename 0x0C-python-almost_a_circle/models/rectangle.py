#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """displays a rectangle using '#'"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """overrides the __Str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """updates attributes"""
        num_args = len(args)
        if num_args > 0:
            self.id = args[0]
        if num_args > 1:
            self.__width = args[1]
        if num_args > 2:
            self.__height = args[2]
        if num_args > 3:
            self.__x = args[3]
        if num_args > 4:
            self.__y = args[4]
