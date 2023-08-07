#!/usr/bin/python3
"""Defines a Rectangle class"""



class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectagnle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance methor returns perimeter"""
        if self.__width != 0 and self.__height != 0:
            return (2 * (self.__width + self.__height))
        else:
            return 0

    def __str__(self):
        """returns a printable rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        r_str = ""
        for i in range(self.__height):
            r_str += str(self.print_symbol) * self.__width + '\n'
        return r_str[:-1]

    def __repr__(self):
        """returns a string representation of rectangle for reporoduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a string when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
    @classmethod
    def square(cls, size=0):
        """returns rectangle instance that is a square"""
        return cls(size, size)
