from Task03 import *
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

    f = open(filename, "r")       # open file to be read
    start = timeit.default_timer()
    for i in f:
        i = i.strip()            # Important thing
        hash_table[i] = 1              # adding each line into the HashTable
        if (timeit.default_timer() - start > 3):
            break
    f.close()                     # closing the file
    return hash_table

def test():

    hash = HashTable()
    load_dictionary(hash, "english_small.txt")

def dictionary_function():
    """

    @complexity: The best case is O(n) and the worst case O()
    """
    b = [1, 27183, 250726]
    Tablesize = [250727, 402221, 1000081]
    filename = ["english_small.txt", "english_large.txt", "french.txt"]

    for i in range(len(filename)):
        name = filename[i]
        print(str(name)+ ": ")
        b_string = "b"
        Tablesize_string = "TableSize"
        end_string = "End Time"
        print("%-5s %-10s %-10s " %(b_string, Tablesize_string, end_string))
        for j in range(len(b)):
            for k in range(len(Tablesize)):
                hash_value = HashTable(Tablesize[k], b[j])
                start_time = timeit.default_timer()
                load_dictionary(hash_value, name)             # load dictionary function
                end_time = timeit.default_timer() - start_time
                end_time = round(end_time, 4)
                if end_time > 3:
                    end_time = "TimeOut"
                print("%-5s %-10s %-10s " %(str(b[j]), str(Tablesize[k]), str(end_time)))
                value = hash_value.statistics()

                print("Collision: "+ str(value[0]) + " Probe Total: " + str(value[1])+" probe_max: " + str(value[2])+ " rehash count: " + str(value[3]))


# dictionary_function()

"""
    english_small.txt: 
        b     TableSize  End Time   
        1     250727     TimeOut    
        Collision: 2217 Probe Total: 1948652 probe_max: 2402 rehash count: 0
        1     402221     TimeOut    
        Collision: 2212 Probe Total: 1940128 probe_max: 2402 rehash count: 0
        1     1000081    TimeOut    
        Collision: 2233 Probe Total: 1975584 probe_max: 2402 rehash count: 0
        27183 250727     0.961      
        Collision: 14263 Probe Total: 22542 probe_max: 21 rehash count: 0
        27183 402221     0.9615     
        Collision: 9012 Probe Total: 11749 probe_max: 13 rehash count: 0
        27183 1000081    0.9472     
        Collision: 3487 Probe Total: 3908 probe_max: 5 rehash count: 0
        250726 250727     TimeOut    
        Collision: 2007 Probe Total: 1975708 probe_max: 2041 rehash count: 0
        250726 402221     0.9862     
        Collision: 9011 Probe Total: 11811 probe_max: 10 rehash count: 0
        250726 1000081    0.9802     
        Collision: 3612 Probe Total: 4054 probe_max: 8 rehash count: 0
    english_large.txt: 
        b     TableSize  End Time   
        1     250727     TimeOut    
        Collision: 2269 Probe Total: 1972898 probe_max: 2464 rehash count: 0
        1     402221     TimeOut    
        Collision: 2246 Probe Total: 1929153 probe_max: 2464 rehash count: 0
        1     1000081    TimeOut    
        Collision: 2237 Probe Total: 1910312 probe_max: 2464 rehash count: 0
        27183 250727     2.9321     
        Collision: 76622 Probe Total: 420481 probe_max: 278 rehash count: 0
        27183 402221     2.5746     
        Collision: 47799 Probe Total: 100117 probe_max: 43 rehash count: 0
        27183 1000081    2.2457     
        Collision: 19038 Probe Total: 24410 probe_max: 15 rehash count: 0
        250726 250727     TimeOut    
        Collision: 2021 Probe Total: 1995871 probe_max: 2089 rehash count: 0
        250726 402221     2.4579     
        Collision: 47902 Probe Total: 101113 probe_max: 51 rehash count: 0
        250726 1000081    2.4976     
        Collision: 19047 Probe Total: 24487 probe_max: 13 rehash count: 0
    french.txt: 
        b     TableSize  End Time   
        1     250727     TimeOut    
        Collision: 2461 Probe Total: 1984906 probe_max: 2393 rehash count: 0
        1     402221     TimeOut    
        Collision: 2473 Probe Total: 2007667 probe_max: 2393 rehash count: 0
        1     1000081    TimeOut    
        Collision: 2481 Probe Total: 2023261 probe_max: 2393 rehash count: 0
        27183 250727     TimeOut    
        Collision: 73449 Probe Total: 373146 probe_max: 212 rehash count: 0
        27183 402221     2.7437     
        Collision: 53376 Probe Total: 125307 probe_max: 64 rehash count: 0
        27183 1000081    2.5225     
        Collision: 21876 Probe Total: 30360 probe_max: 20 rehash count: 0
        250726 250727     TimeOut    
        Collision: 2239 Probe Total: 2028807 probe_max: 2072 rehash count: 0
        250726 402221     2.8425     
        Collision: 53024 Probe Total: 122168 probe_max: 36 rehash count: 0
        250726 1000081    2.6475     
        Collision: 21795 Probe Total: 30185 probe_max: 11 rehash count: 0

    Conclusion:

"""