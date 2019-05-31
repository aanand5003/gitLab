"""

"""
from Task06 import *

def  word_percentage(filename):
    """
     Creating the database and comparing the words of the other file with the saved database
     precondition: filename should exit in the same file directory
    :param filename: A string of the having txt file
    :return: No return value
    @complexity:@comlexity: The best case is O(h) and the Worst case is (m*n*o)
                    where h is the depth of the binary tree.
                    m is number of lines in the text file,
                    n is the number of words in each line
                    and o is the number of the nodes in the binary tree.

    """

    database = Freq()                        # Making Database
    database.add_file("frankenstein.txt")
    print("One file saved in the database")
    database.add_file("PrideandPrejudice.txt")
    print("Second file saved in the database")
    database.add_file("WarAndPeace.txt")
    print("Third file saved in the database")

    array = []
    word_count =0
    #array.append(0)

    # common = 0
    array.append(0)

    #uncommon = 0
    array.append(0)

    #rare = 0
    array.append(0)
    #misspelling = 0
    array.append(0)

    file_data = open(filename, "r", encoding="utf8")
    edit = str.maketrans("", "", string.punctuation)
    for i in file_data:
        i = i.strip()
        i = i.translate(edit)
        array_of_words = i.split()
        for j in range(len(array_of_words)):
            word_lower_case = array_of_words[j].lower()
            word_lower_case = word_lower_case.strip("“")  # The unusual punctuation handing
            word_lower_case = word_lower_case.strip("”")  # using strip to remove from the end and beginning
            word_lower_case = word_lower_case.strip("‘")  # Don't want to remove from the middle
            word_lower_case = word_lower_case.replace("’", "")  # Using replace to replace the value in the middle
            word_lower_case = word_lower_case.replace("—", "")
            word_count += 1

            if database.rarity(word_lower_case) == 0:
                array[0] += 1
            elif database.rarity(word_lower_case) == 1:
                array[1] += 1
            elif database.rarity(word_lower_case) == 2:
                array[2] += 1
            elif database.rarity(word_lower_case) == 3:
                array[3] += 1

    print("%-15s %-15s %-15s %-15s  " % (  "common ", "uncommon ", "rare ", "misspelling "))
    print("%-15s %-15s %-15s %-15s  " % (  str(round(array[0]/word_count *100,2)), str(round(array[1]/word_count * 100,2)),
                                               str(round(array[2]/word_count * 100,2)), str(round(array[3]/word_count * 100,2))))

word_percentage("ATaleOfTwoCities.txt")



"""
Data for the  rarity method

ATaleOfTwoCities.txt is compared with the stored database

common          uncommon        rare            misspelling      
61.71           18.8            14.68           4.81   
"""