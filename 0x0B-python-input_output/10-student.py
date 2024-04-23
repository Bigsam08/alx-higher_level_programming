#!/usr/bin/python3
"""A class Student."""


class Student:
    """initializing class student."""

    def __init__(self, first_name, last_name, age):
        """new Student profile
        Args:
            first_name (str): student first name.
            last_name (str): student last.
            age (int): student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dic rep of student
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
