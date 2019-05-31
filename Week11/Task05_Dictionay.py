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
        hash_table[i] = 1               # adding each line into the HashTable
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
    Tablesize = [ 250727, 402221, 1000081]
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

                print("%-15s %-15s %-15s %-15s %-15s %-15s " %(str(b[j]), str(Tablesize[k]), str(end_time)  , str(value[0]), str(value[1]),str(value[2])))





dictionary_function()

"""

english_small.txt: 
b               TableSize       End Time        Collision:      Probe Total:    probe_max:      rehash count:   
1               250727          18.2067         82467           6229979         323             
1               402221          18.5581         82467           6229979         323             
1               1000081         18.7223         82467           6229979         323             
27183           250727          1.5829          12561           14003           4               
27183           402221          1.7569          8253            8836            4               
27183           1000081         1.4417          3328            3420            3               
250726          250727          73.0534         83769           23573968        846             
250726          402221          1.4857          8217            8784            4               
250726          1000081         1.4068          3437            3541            2               

english_large.txt: 
b               TableSize       End Time        Collision:      Probe Total:    probe_max:      rehash count:   
1               250727          99.5702         192642          31627753        661             
1               402221          105.0904        192642          31627753        661             
1               1000081         96.0015         192642          31627753        661             
27183           250727          4.2516          59209           75426           7               
27183           402221          4.2048          40298           47013           5               
27183           1000081         4.9084          17516           18648           4               
250726          250727          TimeOut         129703          55534846        1244            
250726          402221          4.0047          40221           46958           5               
250726          1000081         4.2765          17540           18699           4               

french.txt: 
b               TableSize       End Time        Collision:      Probe Total:    probe_max:      rehash count:   
1               250727          51.1192         197093          16569022        449             
1               402221          48.854          197093          16569022        449             
1               1000081         49.1571         197093          16569022        449             
27183           250727          3.9055          63487           81572           6               
27183           402221          3.8685          43389           50812           5               
27183           1000081         3.9376          19159           20421           4               
250726          250727          136.7971        199994          45573926        875             
250726          402221          4.1515          42999           50290           5               
250726          1000081         4.092           19118           20418           4               


"""
