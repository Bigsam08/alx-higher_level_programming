#!/usr/bin/python3
""" create a student class """


class Student:
    def __init__(self, first_name, last_name, age):
        """ class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        else:
            return self.__dict__
