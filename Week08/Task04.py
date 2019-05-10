from Task01 import *
from task03 import *
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "10/05/2019"
"""

class Editor:

    def __init__(self):
        """

         @:param:
         @complexity:
        """
        self.text_lines = ListADT();

    def menu(self):
        """
        UI menu to the user to chose the options for the function.
        :return:

        """
        exit = False


        print("read filename\nprint num\ndelete num\ninsert num\ninsert num\nquit")


        while not exit:                         #keep running if user do not enter quit
                step = True
                value = input()
                check = value.split()
                try:
                    command = check[0]
                except IndexError:
                    print("No input")
                    step = False
                if step:
                    if check[0] == "read" :
                        try:

                           self.text_lines = read_text_file(check[1])


                        except:
                            print("?")

                    elif check[0] == "print":
                        # for line 1 = index 0 hence
                        inside = True
                        try:              # checking if there is item or not
                            check[1]      # if not then append 0 to print all elements
                        except:
                            print(self.text_lines)
                            inside = False

                        if inside:


                                try:
                                    if int(check[1]) == 0:
                                        print("?")
                                    else:
                                        print(self.print_num(int(check[1])))
                                except (ValueError, IndexError):

                                    print("?")

                    elif check[0] == "delete":
                        inside = True
                        try:
                            check[1]
                        except IndexError:
                            if len(self.text_lines) > 0:
                                for i in range(len(self.text_lines)):
                                    self.text_lines.delete(0)
                            inside = False



                        if inside:

                            try:
                                if int(check[1]) == 0:
                                    print("?")
                                else:
                                    self.delete_num(int(check[1]))
                            except(ValueError, IndexError):
                                print("?")

                    elif check[0] == "insert":
                        stop = True
                        try:
                            self.text_lines[int(check[1])]
                            if (int(check[1]) == 0):
                                print("?")
                            else:
                                array = ListADT()
                                while stop:
                                    string = input()
                                    if (string == "."):
                                        stop = False
                                    else:
                                        array.append(string)

                                self.insert_num_string(int(check[1]), array)
                        except (ValueError , IndexError):

                                   print("?")
                    elif check[0] == "search":
                        self.search_string(check[1])


                    elif check[0] == "quit":
                         exit = True
                    else:
                        print("?")


    def print_num(self, num):
        """
        @pre-condition: input must be integer to indicate which element will be printed
        @post-condition: return the element given index
        :param num: input must be integer that indicate the position of the element
        :return: the element at the given index
        @complexity: worst and best case: O(1)
        """
        if num > 0:                                         #subtract one from num as array start from 0 not 1
            return (self.text_lines[num -1])


        elif num < 0:
            return (self.text_lines[num])                   #print the element at num if num is negative as negative index start from the very enf of the array, thus no adjustment is needed
    def delete_num(self,num):
        """
        @pre-condition: input must be an integer that indicate the position of the element that will be deleted
        @post-condition: element at given index will be deleted. The array might be resize if the elemnets inside occupied less than 1/4 of the array length.
        @complexity: worst and best case: O(1)
        :param num: input must be integer that indicate the position of the element
        :return:
        """
        if num > 0:                                         #subtract one from num as array start from 0 not 1
            self.text_lines.delete(num-1)                   #deleting the element at num
        elif num < 0:
            self.text_lines.delete(num)                     #delete the element at num, no need of adjustment if num is negative as negative index start from the very enf of the array.

    def insert_num_string(self,number,list_of_strings):
        """
        @pre-condition: input must be an integer and an array
        @post-condition: insert the element at the index of the array
        @complexity: worst case: O(n) where n is the length of the array
                        best case: O(1) if the its the first element in the array
        :param number: index of the array where the input is to be insert
        :param list_of_strings: the array that is to be inserted
        :return:
        """
        if number > 0:                                      #subtract one from number as array start from 0 not 1
            position = number - 1
        if number < 0:
            position = number                               #set postion equal number if number is negative
        for i in range(len(list_of_strings)):               #loop throuht the list of string

            self.text_lines.insert(position,list_of_strings[i])         #inserting the element in the list of striing at position
            if number > 0:
                position += 1                           #increment the position

    def search_string(self, string):
        """
        @pre-condition: input must be a string
        @post-condition: this will search through the array to find any element inside the array that match the input string
        :param string: string that user want to search for
        :return:
        @complexity: worst and best case: O(n^2) where n is the length of the text_line
        """
        store = ListADT()
        j = 0
        step = False
        for i in range(len(self.text_lines)):               #loop through the array
            j = 0
            value = self.text_lines[i]                      #set value as the element at index i of the array
            for k in range(len(self.text_lines[i])):        #loop through each element in the array
                step = True
                if string[j] == value[k]:                   #comparing the string and element at index i letter by letter


                    if len(string) == j+1:
                        store.append(i+1)

                        print(i+1)
                        break

                    else:
                        step = False
                        j += 1
                if step:
                    #step = True
                    j = 0



editor = Editor()
editor.menu()
