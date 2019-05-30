"""

"""
from Task06 import *

def  word_percentage(filename):
    """

    :param filename:
    :return:
    """

    database = Freq()
    database.add_file("frankenstein.txt")
    print("one file saved in the database")
    database.add_file("PrideandPrejudice.txt")
    print("second file saved in the database")
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
        print(word_count)
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
    print(array)
    print(database.max_count)
    print("%-15s %-15s %-15s %-15s  " % (  "common ", "uncommon ", "rare ", "misspelling "))
    print("%-15s %-15s %-15s %-15s  " % (  str(array[0]/word_count *100), str(array[1]/word_count * 100),
                                               str(array[2]/word_count * 100), str(array[3]/word_count * 100)))

word_percentage("ATaleOfTwoCities.txt")

"""
78083
78083
[46150, 15959, 15974, 0]
43422
common          uncommon        rare            misspelling      
59.103774189004014 20.43850774176197 20.45771806923402 0.0    
"""

"""
ATaleOfTwoCities.txt
138836
[85675, 26108, 20383, 6680]
43422
common          uncommon        rare            misspelling      
61.705054520836036 18.80356654134797 14.680293274563185 4.811085663252813  
"""