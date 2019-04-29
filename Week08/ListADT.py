#!/usr/bin/python3
class ListADT:

    def __init__(self, size):
        """

        :param size:
        """
        self.the_array = [None]*size
        self.length = 0
    def __init__ (self):
        """

               :param size:
               """
        self.the_array = [None] * 35
        self.length = 0
    def __str__(self):
        """

        :param self:
        :return:
        """
        word = ""
        if self.is_empty():
            return word
        else:
            for i in range(self.length):
                word += str(self.the_array[i]) + "\n"
        return word

    def __len__(self):
        """

        :param self:
        :return:
        """
        if self.is_empty():
            return 0
        else:
            value = self.length
            return value
    def __getitem__(self, index):
        """

        :param self:
        :param index:
        :return:
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
        if index <= self.length and index >= (-self.length):
                         


               if index < 0:
                   index = self.length + index
               value  = self.the_array[index]
               for i in range(index, self.length):
                   temp = self.the_array[i+1]
                   self.the_array[i+1] = value
                   value = temp

               self.the_array[index] = item
               self.length+=1
        else:
            raise IndexError()

    def delete(self, index):
        """

        :param index:
        :return:
        """
        if index < self.length and index >= (-self.length):
            if index < 0:
                index = self.length + index
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


