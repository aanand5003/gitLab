"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "03/05/2019"
"""


# !/usr/bin/python3
class ListADT:

    def __init__(self, size = 35):
        """

        :param size:
        """
        if size < 35:
            size = 35
        self.the_array = [None] * size
        self.length = 0
        self.size = size

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
        if index <= self.length and index >= (-self.length):
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

        if index < self.length and index >= (-self.length):
            self.the_array[index] = item
        else:
            raise IndexError()

    def __eq__(self, other):
        if len(other) == len(self):
            for i in range(len(self)):
                if other[i] != self.the_array[i]:
                    return False
            return True
    def resize(self):
        if self.is_full():
            new_size = round(self.size*(1.6))+ self.size
            new_the_array = [None]* new_size
        elif (1/4 * self.size > len(self) and self.size >= 70):
            new_size = round(self.size*(0.5))
            new_the_array = [None]* new_size



        for i in range(len(self)):
                new_the_array[i] = self.the_array[i]
        self.size = new_size
        self.the_array = new_the_array



    def insert(self, index, item):
        """
        qUESTION ABOUT THE APPEND OR INSERT IN TH EBETWEEN LAST AND SECOND LAST ELEMENT FOR THE LAST INDEX OR -1
        """
        if index > len(self) or index < (-len(self)) - 1:
            raise IndexError()
        if self.is_full():
            self.resize()

        if index < 0:
            index = self.length + 1 + index
        for i in range(len(self) - 1, index - 1, -1):
            self.the_array[i + 1] = self.the_array[i]
        self.the_array[index] = item
        self.length += 1

    def delete(self, index):
        """

        :param index:
        :return:
        """
        if index > len(self) or index < (-len(self)) - 1:
            raise IndexError()

        if index < 0:
            index = self.length + index
        found = self.the_array[index]
        for i in range(index+1, len(self), 1):
            self.the_array[i-1] = self.the_array[i]
        self.length -= 1
        if(1/4 * self.size > len(self) and self.size >= 70):   # Checking for the resize
                self.resize()
        return found


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
        if self.is_full():
            self.resize()
        self.the_array[self.length] = item
        self.length += 1

        if(1/4 * self.size > len(self) and self.size >= 70):
            self.resize()
    def unsafe_set_array(self, array, length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')

        self.the_array = array
        self.length = length

p = ListADT(12)
print(p.size)
for i in range(9):
    p.append(i)
print(p.size)
print(p.the_array)
for i in range(1):
 size = p.delete(0)



#for i in range(0, 15,1):
   # p.delete(i)

print(p.the_array)
print(len(p))
print(p.size)
