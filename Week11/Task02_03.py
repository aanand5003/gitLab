from Task04 import *
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





dictionary_function()

""" 
    TimeOut, when time > 60 seconds
    english_small.txt: 
    b               TableSize       End Time        Collision:      Probe Total:    probe_max:      rehash count:   
    1               250727          TimeOut         8950            37789240        9172            0               
    1               402221          TimeOut         9050            38658237        9247            0               
    1               1000081         TimeOut         9052            38676569        9271            0               
    27183           250727          1.0155          14263           22542           21              0               
    27183           402221          0.963           9012            11749           13              0               
    27183           1000081         0.9482          3487            3908            5               0               
    250726          250727          TimeOut         8735            37975449        8777            0               
    250726          402221          0.9768          9011            11811           10              0               
    250726          1000081         0.9809          3612            4054            8               0               
    
    english_large.txt: 
    b               TableSize       End Time        Collision:      Probe Total:    probe_max:      rehash count:   
    1               250727          TimeOut         9067            38170537        9228            0               
    1               402221          TimeOut         8955            37207970        9112            0               
    1               1000081         TimeOut         8901            36750459        9112            0               
    27183           250727          2.9929          76622           420481          278             0               
    27183           402221          2.4089          47799           100117          43              0               
    27183           1000081         2.2515          19038           24410           15              0               
    250726          250727          TimeOut         8618            36955118        8662            0               
    250726          402221          2.5029          47902           101113          51              0               
    250726          1000081         2.6112          19047           24487           13              0               
    
    french.txt: 
    b               TableSize       End Time        Collision:      Probe Total:    probe_max:      rehash count:   
    1               250727          TimeOut         10594           36422434        10991           0               
    1               402221          TimeOut         10561           36117416        10991           0               
    1               1000081         TimeOut         10727           37695386        10991           0               
    27183           250727          3.5953          84347           563708          363             0               
    27183           402221          2.8446          53376           125307          64              0               
    27183           1000081         2.6596          21876           30360           20              0               
    250726          250727          TimeOut         10402           36952373        9648            0               
    250726          402221          2.8784          53024           122168          36              0               
    250726          1000081         2.6827          21795           30185           11              0     

    Conclusion: 
    According to the Table, when it's more collision and having the largest probing the base value and the Tablesize got the 
    TimeOut ( TimeOut time > 60 sec) 
    Longest Probe chain is the when b = 1 and the TableSize = 1000081 which does not differ from the rest of the value of 
    b = 1 which disobey the promise of the HashTable( O(1)) the reason behind is because of the probe chain and the 
    collision. Having b = 1 doesn't given a wide spectrum of hash values results, values insert closely in the Hash Table
    and results to increment of the probe chain in every setitem. It better to use the base value which has larger value as
    well as having larger table capacity.
    The number of the lines always less the Table capacity, as I checked the maximum numbers of the line from the given text
    file which is slightly less than the lowest value of the given table capacity. Hence there is no point to rehashing. 
    
        

"""