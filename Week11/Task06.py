"""
@name: Shourya raj
@email id: sraj0008@student.monash.edu
@created on: 31/05/2019

"""
from Task06_HashTable import *
import string
class Freq:

    def __init__(self):
        self.max_count = 0
        self.max_word_appear = ""
        self.hash_table = HashTable()

    def add_file(self, filename):
        try:
            f = open(filename, "r", encoding = "utf8")


        except ValueError:
            print("Name should be an string")

        f = open(filename, "r", encoding= "utf8")  # open file to be read
        edit = str.maketrans("", "", string.punctuation)

        for i in f:
            i = i.strip()            # Important thing
            i = i.translate(edit)    # Translating for no punctuation, but there are weird punctuation still left

            array_of_words = i.split()    # Array of words

            for j in range(len(array_of_words)):
                word_lower_case = array_of_words[j].lower()
                word_lower_case = word_lower_case.strip("“")    # The unusual punctuation handing
                word_lower_case = word_lower_case.strip("”")    # using strip to remove from the end and beginning
                word_lower_case = word_lower_case.strip("‘")    # Don't want to remove from the middle
                word_lower_case = word_lower_case.replace("’", "")  # Using replace to replace the value in the middle
                word_lower_case = word_lower_case.replace("—", "")
                if(word_lower_case in self.hash_table):
                    count = self.hash_table[word_lower_case]  # Getting number of counts
                    count += 1
                    if count > self.max_count:
                        self.max_count = count
                        self.max_word_appear = word_lower_case
                else:
                    count = 1
                self.hash_table[word_lower_case] = count  # adding each line into the HashTable
        f.close()                                         # closing the file
        return self.hash_table

    def rarity(self, given_word):
        """
    
        :param given_word: It takes an value of string
        :return: Return the value from 0 to 3 according to frequency of word  
        """
        if not given_word.lower() in self.hash_table:
            retVal =  3
        else:
            frequency = self.hash_table[given_word.lower()]
            if frequency >= self.max_count / 100:
                retVal = 0
            elif frequency < self.max_count / 1000:
                retVal = 2
            else:
                retVal = 1

        return retVal

# x = Freq()
# #x.add_file("PrideAndPrejudice.txt")
# print("done 1")
# x.add_file("frankenstein.txt")
# # print("done 2")
#
# for i in range(5000):
#     if x.hash_table.array[i] is not None:
#           print(x.hash_table.array[i][0])
#           print(x.hash_table.array[i][1])
#
# print(x.max_word_appear )
# print(x.max_count)
#
# print(x.rarity("off"))
# print(x.rarity("the"))