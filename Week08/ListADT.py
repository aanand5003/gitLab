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
        Returns the length of the list.

        :param          the_list data structure
        :return         the length of the list
        :complexity     best and worst case: O(1)
        """
        if self.is_empty():
            return 0
        else:
            value = self.length
            return value
    def __getitem__(self, index):
        """
        Returns an item at a given position in the list.
        :param self: the_list data structure
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
         Sets the value at index in the list to be item
        :param self: the_list data structure
        :param index: It should be an integer value.
        :param item:  The value to be set at that index
        @complexity: best is O(length) and worst case O(1):
        """

        if index < self.length and index >= (-self.length):
            self.the_array[index] = item
        else:
                raise IndexError()

    def __eq__(self, other):
        """
        Returns True if this list is equivalent to other otherwise return FALSE.
        :param other: the list_data type
        :return: The Boolean value for the equality of the given array and the self array.
        """
        if len(other) == len(self):
           for i in range(len(self)):
               if other[i] != self.the_array[i]:
                   return False
           return True

    def insert (self, index, item):
        """
         Inserts the given item at the given position in the list.
        :param index: An integer value
        :param item:  The value which is going to inserted in the the array
        @complexity:  best is O(length) and worst case O(1):
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

        Deletes the first appearance (if any) of the input item.

        :param      the_list data structure
        :param      inex of the item to be deleted
        :return     Return  item if it is the deleted.
        :post       if item was in list, list has one fewer elements
        :complexity best and worst case: O(length)
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
        Determines if the list has any elements.

        :param          the_list data structure
        :return         false if list has elements, true if empty
        :complexity     best and worst case: O(1)
        """
        return self.length == 0

    def is_full(self):
        """
        Determines whether the list is full.
        Since it is implemented with arrays, it can get full.

         @param      the_list data structure
         @return     true is the list is full, false otherwise
         @complexity best and worst case: O(1)
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """
        Check the given item is contain in the list data structure.
        :param item: The value of the to be checked in the the list data structure
        :return: The Boolean Value after the checking the item.
        @complexity: The best case(1) and the worst case O(m).
        """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False

    def append(self, item):
        """
        :param:         new_item to add to this list
        @post           raise expection when list is full.
        @complexity     best and worst case: O(1)
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