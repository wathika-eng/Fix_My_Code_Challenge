#!/usr/bin/python3
"""Calculate area and perimeter of a square"""


class square:
    """
    Represents a square with specified width and height.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a Square object with the given width and height.

        area(self) -> int:
            Calculates and returns the area of the square.

        perimeter(self) -> int:
            Calculates and returns the perimeter of the square.

        __str__(self) -> str:
            Returns a string representation of the square, including its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Square object with the given width and height.

        Args:
            width (int): The width of the square.
            height (int): The height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def PerimeterOfMySquare(self):
        """
        Calculates and returns the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.width

    def __str__(self):
        """
        Returns a string representation of the square, including its width and height.

        Returns:
            str: A string representation of the square.
        """

        return f"{self.width}, {self.height}"


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
