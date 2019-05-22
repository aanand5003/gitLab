from Task01 import *
import timeit
"""
@name: shourya raj
@email id: sraj0008@student.monash.edu
@created on: /05/2019

"""

def load_dictionary(hash_table, filename):
    """
        Reads each line of text into a string, returning a list of strings associated to the file
        :param name: The String name of the file
        :return: A list of an string having all lines of the text file.
        @post: An ADT type of list.
        @complexity: The best case and the worst case O(length) where length is the lines of the text file.
        """
    try:
        f = open(filename, "r")

    except ValueError:
        print("name should be an string")
    start = timeit.default_timer()
    f = open(filename, "r")       # open file to be read
    for i in f:
        hash_table[i] = 1 # adding each line into the HashTable
        if (timeit.default_timer() - start > 3):
            break
    f.close()                     # closing the file
    return hash_table

def test():
    hash = HashTable()
    load_dictionary(hash, "english_small.txt")
def dictionary_function():
    """

    :return:
    """
    b = [1, 27183, 250726]
    Tablesize = [250727, 402221, 1000081]
    filename = ["demo.txt", "english_small.txt", "english_large.txt", "french.txt"]

    for i in range(len(filename)):
        name = filename[i]
        print(str(name)+ ": " +"\n")
        for j in range(len(Tablesize)):
            hash_value = HashTable(Tablesize[j], b[j])
            start_time = timeit.default_timer()
            load_dictionary(hash_value, name)
            end_time = timeit.default_timer() - start_time
            end_time = round(end_time, 4)
            print( "b " + "  TableSize " + " end_time")
            print(str(b[j]) + " "+str(Tablesize[j]) +" "+ str(end_time))


dictionary_function()