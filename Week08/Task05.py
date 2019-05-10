from Task01 import *
from task03 import *
from stackADT import *

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
         @complexity: worst and best case: O(1)
        """
        self.text_lines = ListADT();
        self.text_Stack = Stack();


    def menu(self):
        """
        UI menu to the user to chose the options for the function and proceed the function.
        :return:

        """
        exit = False


        print("read filename\nprint num\ndelete num\ninsert num\ninsert num\nquit")


        while not exit:
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

                           self.read_filename(check[1])


                        except:
                            print("?")

                    elif check[0] == "print":
                        # for line 1 = index 0 hence
                        inside = True
                        try:
                            if len(check) == 1:
                                print(self.print_num())
                                inside = False

                            if inside:

                                if int(check[1]) == 0:
                                    print("?")
                                else:
                                    print(self.print_num(int(check[1])))
                        except (ValueError, IndexError):

                                    print("?")

                    elif check[0] == "delete":
                        inside = True
                        try:
                            if len(check) == 1:
                                self.delete_num()
                                inside = False

                            if inside:
                                    if int(check[1]) == 0:
                                        print("?")
                                    else:
                                        arr = ListADT()
                                        self.text_Stack.push(int(check[1]))
                                        if int(check[1]) > 0:

                                            arr.append(self.text_lines[int(check[1]) - 1])
                                        else:
                                            arr.append(self.text_lines[int(check[1])])
                                        arr.append(0)  # for the delete 0
                                        self.text_Stack.push(arr)
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
                                        array.append(string + "\n")
                                array.append(1)            # for insert 1
                                arr = array


                                self.text_Stack.push(int(check[1]))
                                self.text_Stack.push(arr)
                                self.insert_num_string(int(check[1]), array)  # changed here from array to array[0]
                        except (ValueError , IndexError):
                                print("?")

                    elif check[0] == "search":
                        # Making an string
                        word =""

                        for i in range(len(check)-1):
                            if(i == len(check)-2):
                                word += check[i + 1]
                            elif (i != len(check)-1 and len(check) > 2):
                               word += check[i+1]+" "  # last element handle
                            else:
                                word +=check[i+1]

                        try:
                            value = self.search_string(word)

                            if len(value) != 0:
                                print("Given String appeared in the following line")
                                for i in range(len(value)):
                                    print(value[i])
                            else:
                                print("Give String dosen't appeard in the text")
                        except:
                            print("?")

    def read_filename(self, value):
        """
          :param name: The String name of the file
          @post: An ADT type of list.
          @complexity: The best case and the worst case O(length) where length is the lines of the text file.
        """
        self.text_lines = read_text_file(value)
    def print_num(self, num = "all"):
        """
        @pre-condition: input num will indicate which element in the array will be printed out
        @post-condition: the element at the given index will be printed
        @complexity: worst and best case: O(1)
        :param num: the index of the array and initial value 0 to print all value.
        :return: the element at the index
        """

        if num == "all":
            return self.text_lines
        elif num == 0:
            raise Exception("No zero please")
        elif num > 0:
            return (self.text_lines[num -1])            #return the element at num-1 as array start from 0 and the input from user start from 1
        elif num < 0:
            return (self.text_lines[num])               #return the element at num as negative index start from the last element of the array

    def delete_num(self,num = "all"):
        """
        @pre-condition: input should be an integer that indicate the position of the element in the array to be deleted
        @post-condition: the element at the given index will be deleted
        @complexity: worst and best case: O(1)
        :param num: index at which the element will be deleted
        :return:
        """
        if num == "all":
            if len(self.text_lines) > 0:
                for i in range(len(self.text_lines)):
                    self.text_lines.delete(0)
        elif num == 0:
            raise Exception("Not is range")
        elif num > 0:
            item = self.text_lines.delete(num-1)                #deleting the element at the given index by calling delete function from ListADT

        elif num < 0:
            item = self.text_lines.delete(num)
          #deleting the element at the given index by calling delete function from ListADT


    def insert_num_string(self,number,list_of_strings):
        """
        @pre-condition: number that indicate where the string should insert from and the string that will be inserted
        @post-condition: insert the string at the given index
        @complexity: worst case: O(n) where n is the length of the list_of_string
                        best case: O(1) the first element in the array
        :param number: the index of the array
        :param list_of_strings: what to insert at the given index
        :return:
        """
        if number == 0:
            raise Exception("Can't add anything at zero line")
        elif number > 0:
            position = number - 1               #array start from 0 not 1
        elif number < 0:
            position = number                   #otherwise, set number as position

        if (list_of_strings[-1] == 1):          # checking for the last bit == 1 ( 1 is to check the insert function happen that time)
            length = len(list_of_strings)-1
        else:
            length = len(list_of_strings)
        for i in range(length):                 #loop through the list of string without t

            self.text_lines.insert(position,list_of_strings[i])         #inserting the string at the position
            if number > 0:
                position += 1                   #increase the position by 1

    def search_string(self, string):
        """
        @pre-condition: input should be a string that will be compared to each element in the array
        @post-condition:
        :param string: string that needed to search
        :return: store
        @complexity: worst case: O(mn^2) where n is the length of the text_line and m is the length of the string
        """
        store = ListADT()
        j = 0
        step = False
        for i in range(len(self.text_lines)):                       #loop through every elements inside the array
            j = 0
            value = self.text_lines[i]                                 #set value as the element at index i
            if (len(value) >= len(string)):   #)len(value(-1                  #check if length of the element at index i is longer than the given string since the given string can not be the same as element at index i if it is longer than that element

               for k in range(len(self.text_lines[i])):  #-1          #loop through the string at index i
                    step = True
                    word = ""
                    if k+len(string) <= len(value):
                        for l in range(len(string)):                #loop through the given string
                            index = k+l
                            word += value[index]
                        if string == word:
                            store.append(i+1)

                            break
        return store

