#!/usr/bin/python3
class ListADT:

    def __init__(self, size = 35):
        """
         Creates an empty list with given size, and length 0.
        :param size: It should be an Integer.
        :complexity:  best and worst case: the complexity of [None]*size, which it is
                      probably O(size)
        """
        try:
            size = int(size)
        except:
            raise(" Size is not a number")
        self.the_array = [None]*size
        self.length = 0

    def __str__(self):
        """
        Returns a string representation of the list
        :param self: The ListADT class
        :return:  String of List item having one item per line.
        :complexity: the best case is O(1) and the worst case would be the O(self.length)
        """
        word = ""
        if not self.is_empty():
            for i in range(self.length):
                word += str(self.the_array[i]) + "\n"
        return word

    def __len__(self):
        """
         Returns the number of elements in the the_array
        :param self: The ListADT class
        :return: the length of the the_array (self.length) or 0
        :complexity: he best case is O(1) and the worst case is 0(1)
        """
        if self.is_empty():
            return 0
        else:
            value = self.length
            return value
    def __getitem__(self, index):
        """
           Returns an item at a given position in the list.
        :param self:the_list data structure
        :param index: It should be an integer value.
        :return: the item at index in the_array
        """
        if index <= self.length  and index >= (-self.length):
            item = self.the_array[index]
        else:
           raise IndexError()



        return item

    def __setitem__(self, index, item):
        """

        :param self:
        :param index:
        :param item:
        :return:
        """

        if index < self.length  and index >= (-self.length):
            self.the_array[index] = item
        else:
                raise IndexError()

    def __eq__(self, other):
       if len(other) == len(self):
           for i in range(len(self)):
               if other[i] != self.the_array[i]:
                   return False
           return True










    def insert (self, index, item):
        """
        qUESTION ABOUT THE APPEND OR INSERT IN TH EBETWEEN LAST AND SECOND LAST ELEMENT FOR THE LAST INDEX OR -1
        """
        if index > len(self) or index < (-len(self))-1:
            raise IndexError()
        if self.is_full():
            raise StopIteration("The List is full")

        if index < 0:
            index = self.length +1 + index
        for i in range(len(self) - 1, index - 1, -1):
            self.the_array[i + 1] = self.the_array[i]
        self.the_array[index] = item
        self.length += 1

    def delete(self, index):
        """

        :param index:
        :return:
        """
        if index < self.length and index >= (-self.length):
            if index < 0:
                index = self.length + index + 1
            found = self.the_array[index]
            for i in range(index, self.length - 1):
                self.the_array[i] = self.the_array[i + 1]
            self.length -= 1
            return found
        else:
            raise IndexError()
    def is_empty(self):
        """

        :return:
        """
        return self.length == 0

    def is_full(self):
        """

        :return:
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """

        :param item:
        :return:
        """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False
 
    def append(self, item):
        """

        :param item:
        :return:
        """
        if not self.is_full():
            self.the_array[self.length] = item
            self.length +=1
        else:
            raise Exception('List is full')

    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')

        self.the_array = array
        self.length = length


p = ListADT()
k = ListADT(35)
p.append(0)
p.append(1)
p.append(2)
k.append(1)
p.insert(-4,11)
print(p.the_array)
print(k.the_array)