from Task01 import *
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "03/05/2019"
"""

#!/usr/bin/python3


def read_text_file(name):
    """
    Reads each line of text into a string, returning a list of strings associated to the file
    :param name: The String name of the file
    :return: A list of an string having all lines of the text file.
    @post: An ADT type of list.
    @complexity: The best case and the worst case O(length) where length is the lines of the text file.
    """
    try:
        f = open(name, "r")

    except ValueError:
        print("name should be an string")

    array_string = ListADT()
    f = open(name, "r")
    for i in f:
        array_string.append(i)
    f.close()
    return array_string
