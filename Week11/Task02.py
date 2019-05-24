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

    f = open(filename, "r")       # open file to be read
    start = timeit.default_timer()
    for i in f:
        i = i.strip()
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
    filename = [ "english_small.txt", "english_large.txt", "french.txt"]

    for i in range(len(filename)):
        name = filename[i]
        print("\n"+ str(name)+ ": ")
        b_string = "b"
        Tablesize_string = "TableSize"
        end_string = "End Time"
        print("%-15s %-15s %-15s " % (b_string, Tablesize_string, end_string))
        for j in range(len(b)):
            for k in range(len(Tablesize)):
                hash_value = HashTable(Tablesize[k], b[j])
                start_time = timeit.default_timer()
                load_dictionary(hash_value, name)
                end_time = timeit.default_timer() - start_time
                end_time = round(end_time, 4)
                if end_time > 3:
                    end_time = "TimeOut"
                print("%-15s %-15s %-15s " % (str(b[j]), str(Tablesize[k]), str(end_time)))

dictionary_function()

"""
     english_small.txt: 
    b               TableSize       End Time        
    1               250727          TimeOut         
    1               402221          TimeOut         
    1               1000081         TimeOut         
    27183           250727          0.9234          
    27183           402221          0.9123          
    27183           1000081         0.895           
    250726          250727          TimeOut         
    250726          402221          0.9531          
    250726          1000081         0.9296          
    
    english_large.txt: 
    b               TableSize       End Time        
    1               250727          TimeOut         
    1               402221          TimeOut         
    1               1000081         TimeOut         
    27183           250727          2.4747          
    27183           402221          2.1436          
    27183           1000081         2.1159          
    250726          250727          TimeOut         
    250726          402221          2.3454          
    250726          1000081         2.1334          
    
    french.txt: 
    b               TableSize       End Time        
    1               250727          TimeOut         
    1               402221          TimeOut         
    1               1000081         TimeOut         
    27183           250727          TimeOut         
    27183           402221          2.592           
    27183           1000081         2.6035          
    250726          250727          TimeOut         
    250726          402221          2.6692          
    250726          1000081         2.6056    
        
    Conclusion:
    As we can see the from the graph value having less base and value having less difference in between the table capacity 
    and the base value displayed TimeOut.
    It is because of the more Collision occur while setting the value. The reason behind having more Collision is 
    same hash value. According to the formula of Hash value, value =(value*base_value + ord(key[i])) % table_capacity, 
    so the having less base_value gives less spectrum of the range position because of the bounded capacity.
    In the case of the less difference in between the table capacity and the base value, collision happens always with
    start position and the end position because rehashing value always gives close to that position due to the formula 
    we are taking the modulus which is nearer to the value of the base value.
    Hence those values's Time are TimeOut
    
       
    
    
    

"""