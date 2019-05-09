from Task01 import *
from task03 import *
from stackADT import *
import copy
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
        self.text_Stack = Stack();
        self.length = 0;

    def menu(self):
        """
        UI menu to the user to chose the options for the function.
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

                           self.text_lines = read_text_file(check[1])


                        except:
                            print("?")

                    elif check[0] == "print":
                        # for line 1 = index 0 hence
                        inside = True

                        if (len(check) == 1):
                          for i in range(len(self.text_lines)):
                             print(self.text_lines[i])
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
                                    arr = ListADT()
                                    self.text_Stack.push(int(check[1]))
                                    if int(check[1]) > 0:

                                        arr.append(self.text_lines[int(check[1])-1])
                                    else:
                                        arr.append(self.text_lines[int(check[1])])
                                    arr.append(0)               # for the delete 0
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
                                if int(check[1]) > 0:
                                    self.text_Stack.push(int(check[1]))

                                else:
                                    self.text_Stack.push(int(check[1]))
                                self.text_Stack.push(arr)

                                self.insert_num_string(int(check[1]), array)
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



                    elif check[0] == "undo":
                        value = self.undo()
                    elif check[0] == "quit":
                         exit = True
                    else:
                        print("?")


    def print_num(self, num):
        if num > 0:

            return (self.text_lines[num -1])


        elif num < 0:
            return (self.text_lines[num])
    def delete_num(self,num):
        if num > 0:
            item = self.text_lines.delete(num-1)
            print(item)
        elif num < 0:
            self.text_lines.delete(num)

    def insert_num_string(self,number,list_of_strings):
        if number > 0:
            position = number - 1
        if number < 0:
            position = number
        for i in range(len(list_of_strings)-1):

            self.text_lines.insert(position,list_of_strings[i])
            if number > 0:
                position += 1

    def search_string(self, string):
        store = ListADT()
        j = 0
        step = False
        for i in range(len(self.text_lines)):
            j = 0
            value = self.text_lines[i]
            if (len(value) - 1 >= len(string)):

               for k in range(len(self.text_lines[i])-1):
                    step = True
                    word = ""
                    if k+len(string) <= len(value):
                        for l in range(len(string)):
                            index = k+l
                            word += value[index]
                        if string == word:
                            store.append(i+1)

                            break
        return store


    def undo(self):
        array = self.text_Stack.pop()
        index = self.text_Stack.pop()

        if (array[len(array)-1]) == 0:

           list = ListADT()
           item = array.delete(len(array)-1)

           list.append(array)
           list.append(item)
           print(list.the_array)

           self.insert_num_string(index,list)


        elif (array[len(array)-1]) == 1:
            array.delete(len(array)-1)
            for i in range (len(array)):
                if index < 0:
                   index+=1
                self.delete_num(index)

editor = Editor()
editor.menu()
