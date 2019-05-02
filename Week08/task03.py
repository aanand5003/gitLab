from Task01 import *
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "03/05/2019"
"""

#!/usr/bin/python3


def read_text_file(name):
    array_string = ListADT()
    f = open(name, "r")
    for i in f:
        array_string.append(i)
    f.close()
    return array_string
