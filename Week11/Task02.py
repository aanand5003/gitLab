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
        if (timeit.default_timer() - start > 60):
            break
    f.close()                     # closing the file
    return hash_table


def dictionary_function():
    """

     Function is to the analysing the data by printing tables.
     @complexity: The best case is O(n) and the worst case O(n^2)
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
                if end_time > 60:
                    end_time = "TimeOut"
                print("%-15s %-15s %-15s " % (str(b[j]), str(Tablesize[k]), str(end_time)))

# dictionary_function()

"""
     english_small.txt: 
    b               TableSize       End Time        
    1               250727          TimeOut         
    1               402221          TimeOut         
    1               1000081         TimeOut         
    27183           250727          0.9362          
    27183           402221          0.916           
    27183           1000081         0.9043          
    250726          250727          TimeOut         
    250726          402221          1.0235          
    250726          1000081         1.0376          
    
    english_large.txt: 
    b               TableSize       End Time        
    1               250727          TimeOut         
    1               402221          TimeOut         
    1               1000081         TimeOut         
    27183           250727          2.7563          
    27183           402221          2.3357          
    27183           1000081         2.2055          
    250726          250727          TimeOut         
    250726          402221          2.3587          
    250726          1000081         2.2112          
    
    french.txt: 
    b               TableSize       End Time        
    1               250727          TimeOut         
    1               402221          TimeOut         
    1               1000081         TimeOut         
    27183           250727          2.9419          
    27183           402221          2.6587          
    27183           1000081         2.5204          
    250726          250727          TimeOut         
    250726          402221          2.8709          
    250726          1000081         2.8885     
        
    Analysis:
    According to the Table the value of base is greater as well as value having more difference in between the table capacity 
    and base value gives fastest Hashing. In my point of view, the formula we are using to get the hash value is depended
    upon two things base value and the table capacity, the greater the base value and the greater the Table capacity as well as 
    having more difference in between the table capacity gives wide spectrum of the hash value means less collision and 
    even less probing
    
        
    Conclusion:

    As we can see from the Table value, having less base and value having less difference in between the table capacity 
    and the base value displayed TimeOut.
    It is because of the more Collision occur while setting the value. The reason behind having more Collision is 
    the same hash value. According to the formula of Hash value, value =(value*base_value + ord(key[i])) % table_capacity, 
    so the having less base_value gives less spectrum of the range position because of the bounded capacity.
    In the case of the less difference between the table capacity and the base value, collision happens always with
    start position and the end position because rehashing value always gives close to that position due to the formula 
    we are taking the modulus which is nearer to the value of the base value. Results give more collision and probe increases
    as it add more item in the array.
    Hence those values' Time is TimeOut.

    
       
    
"""