"""
@name: shourya raj
@email id: sraj0008@student.monash.edu
@created on: 31/05/2019
"""

class HashTable:


    def  __init__(self, table_capacity = 101, hash_base =31):
        """
            Constructor to initialize the values for the HashTable class
            :param table_capacity: An integer value for the table capacity to make an array
            :param hash_base: An integer value for the hash base to calculate the hash value
        """

        self.table_capacity = table_capacity
        self.array = [None]*table_capacity
        self.hash_base = hash_base
        self.count = 0
        self.collision_count =0
        self.probe_max = 0
        self.probe = 0
        self.probe_total = 0
        self.rehash_count = 0
        #self.probe_array = []
        self.primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
                          919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
                          17519, 21023, 25229, 30293, 36353, 43627, 52361, 62851, 75431, 90523, 108631, 130363, 156437,
                          187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
                          1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]

    def hash(self, key):
        """

        :param key: Any string value
        :return: The calculated hash value with resolved collision
        @complexity: The best case 0(1) and the worst case O(n)
        """
        base = self.hash_base
        value = 0
        for i in range(len(key)):
            value = (value*base + ord(key[i])) % self.table_capacity
        return value

    def __getitem__(self, key):
        """

        :param key: Any string value
        :return:  Value associated with the key
        @complexity: The best case O(1) and the worst case(n) where n is the table size
        @post_condition: If the key is invalid then return KeyError

        """
        position = self.hash(key)
        for _ in range(self.table_capacity):
            if self.array[position] is None:
                raise KeyError(key)
            elif self.array[position][0] == key:
                 return self.array[position][1]
            else:

                position = (position + 1) % self.table_capacity
        raise KeyError(key)

    def __setitem__(self, key, value):
        """

        :param key: An String Value
        :param value: Any value need to set as associate with the key
        :return: No return value
        @complexity: The best case O(1) and the worst case O(m*(n+i)) where i is prime array length , n is the length of
        the old array
        @post_condition: Value would be assigned in the array
        """
        position = self.hash(key)
        self.probe = 0
        if self.array[position] is not None:             # It's a collision if there is no space
            self.collision_count += 1

        for _ in range(self.table_capacity):             # loop

           if self.array[position] is None:
               self.array[position] = (key, value)
               self.count += 1
               #self.probe_array.append(self.probe)

               return
           elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return
           else:
               position = (position + 1) % self.table_capacity
               self.probe += 1
               self.probe_total += 1
               if self.probe > self.probe_max:
                   self.probe_max = self.probe


        self.rehash()
        self.__setitem__(key, value)


    def __contains__(self, key):
        """

        :param key: An string value provided by the user
        :return: No return Value
        @complexity: The best case O(1) and the worst case O(M*n) where M is the length of the key.
        """
        position = self.hash(key)
        for _ in range(self.table_capacity):
            if self.array[position] is None:
               return False
            elif self.array[position][0] == key:
                return True
            else:

                position = (position + 1) % self.table_capacity

    def rehash(self):
        """
        It increase the capacity and re-calcuating hash of each item according to the capacity
        @complexity: The best case O(n) and the worst case O(n + i ) where i is prime array length , n is the length of
        the old array
        """
        for i in range(len(self.primes)):
            if self.primes[i] > self.table_capacity * 2:
                new_table_capacity = self.primes[i]
                break
        if new_table_capacity == self.table_capacity:
            raise Exception("Not rehashed the value")
        self.table_capacity = new_table_capacity
        old_array = self.array
        self.array = [None] * new_table_capacity
        # print("old" + str(len(old_array)))
        # print(len(self.array))
        for i in range(len(old_array)):
            self.__setitem__(old_array[i][0], old_array[i][1])
        self.rehash_count += 1

        self.probe = 0


    def statistics(self):
        """
        Returns the value of the counts of collision, probe, rehash
        :return: The Tuple having the value collision count, probe total, probe max, rehash count
        """
        #self.probe_max =max(self.probe_array)
        #self.probe_total =sum(self.probe_array)
        value = (self.collision_count, self.probe_total, self.probe_max, self.rehash_count)
        return value
