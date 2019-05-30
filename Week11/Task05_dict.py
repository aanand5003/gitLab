from Task05 import *
import timeit
"""
@name: shourya raj
@email id: sraj0008@student.monash.edu
@created on: 24/05/2019

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

    f = open(filename, "r")       # open file to be read
    start = timeit.default_timer()
    for i in f:
        i = i.strip()            # Important thing
        hash_table[i] = 1              # adding each line into the HashTable
        if (timeit.default_timer() - start > 180):
            break
    f.close()                     # closing the file
    return hash_table

def test():

    hash = HashTable()
    load_dictionary(hash, "english_small.txt")

def dictionary_function():
    """
    Function is to the analysing the data by printing tables.
    @complexity: The best case is O(n) and the worst case O(n^2)
    """
    b = [1, 27183, 250726]
    Tablesize = [250727, 402221, 1000081]
    filename = ["english_small.txt", "english_large.txt", "french.txt"]

    for i in range(len(filename)):
        name = filename[i]
        print("\n"+str(name)+ ": ")
        b_string = "b"
        Tablesize_string = "TableSize"
        end_string = "End Time"
        print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s " %(b_string, Tablesize_string, end_string, "Collision: ", "Probe Total: ", "probe_max: ", "rehash count: "))
        for j in range(len(b)):
            for k in range(len(Tablesize)):
                hash_value = HashTable(Tablesize[k], b[j])
                start_time = timeit.default_timer()
                load_dictionary(hash_value, name)             # load dictionary function
                end_time = timeit.default_timer() - start_time
                end_time = round(end_time, 4)
                if end_time > 180:
                    end_time = "TimeOut"

                value = hash_value.statistics()

                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s " %(str(b[j]), str(Tablesize[k]), str(end_time), str(value[0]), str(value[1]),str(value[2]), str(value[3])))