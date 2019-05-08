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
        if num > 0:
            return (self.text_lines[num -1])


        elif num < 0:
            return (self.text_lines[num])
    def delete_num(self,num):
        if num > 0:
            self.text_lines.delete(num-1)
        elif num < 0:
            self.text_lines.delete(num)

    def insert_num_string(self,number,list_of_strings):
        if number > 0:
            position = number - 1
        if number < 0:
            position = number
        for i in range(len(list_of_strings)):

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
            for k in range(len(self.text_lines[i])):
                step = True
                if string[j] == value[k]:


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
