#!/usr/bin/python3
""" A locked class """


class LockedClass:
    """
        Prevents a user from dynamically creating a new instance attributes
        except when 'first name' is being entered
    """
    __slots__ = ["first_name"]
