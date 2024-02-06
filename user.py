#!/usr/bin/python3
""" 
User class
"""


class User:
    """
    Represents a user with an email address.

    Attributes:
        __email (str): The email address of the user.

    Methods:
        __init__():
            Initializes a User object with the email attribute set to None.

        email (property):
            Gets the email address of the user.

        email (setter):
            Sets the email address of the user. Raises a TypeError if the input is not a string.
    """

    def __init__(self):
        """
        Initializes a User object with the email attribute set to None.
        """
        self.__email = None

    @property
    def email(self):
        """
        Gets the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Sets the email address of the user. Raises a TypeError if the input is not a string.

        Args:
            value (str): The email address to set.

        Raises:
            TypeError: If the input is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
