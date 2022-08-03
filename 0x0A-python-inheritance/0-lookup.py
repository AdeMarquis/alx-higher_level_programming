#!/usr/bin/python3
"""Function that returns the list of available attributes
and method of and object
"""


def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """

    return dir(obj)
