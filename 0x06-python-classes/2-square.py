#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new Square class.

        Args:
        size (int, optional): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
