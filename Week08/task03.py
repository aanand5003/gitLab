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
    num = 0
    f = open(name, "r")
    for i in f:
        array_string.append(i)
        num +=1
    f.close()
    return array_string
# test
list = read_text_file("story.txt")
satify = 1
f = open("story.txt", "r")
line = f.readline()
i = 0
while line:
    if (list[i] != line):
      satify = -1
      print("wrong")
      break;


    line = f.readline()
    i+=1
f.close()
if (satify == 1):
    print("Satisfy")


f.close()