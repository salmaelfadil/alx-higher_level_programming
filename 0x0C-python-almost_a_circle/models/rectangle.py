#!/usr/bin/python3
"""Rectangle class"""
from base import Base


class Rectangle(Base):
    """Represents a Rectangle"""
    def __init__(self, x, y, width, height, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
