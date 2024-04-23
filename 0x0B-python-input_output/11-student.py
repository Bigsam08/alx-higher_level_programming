#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """defining a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Studet """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student"""
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        """
        for s, p in json.items():
            setattr(self, s, p)
