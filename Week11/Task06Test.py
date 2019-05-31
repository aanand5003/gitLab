"""
@shoourya Raj
@28963555
@
"""

import Task06

import math

import unittest

class FreqTest(unittest.TestCase):


    def test_add_file(self):
        """
         Unit test function to test the rarity function of the Task06 to create a database
        :return:
        """
        x = Task06.Freq()
        z = x.add_file("demo_small.txt")
        f = open("demo_small.txt", "r", encoding="utf8")
        counts_lines = 0
        for i in f:
            counts_lines += 1
            i = i.strip()
            self.assertEqual(i in z, True, msg = "Value should be there in the hashTable")
        self.assertEqual(z.count, counts_lines, msg="single word per line should be equal to the "
                                                    "count of the elements inserted")
        z = x.add_file("frankenstein.txt")
        self.assertEqual("...." in z, False, msg = "should not exits")
        self.assertEqual("the" in z, True, msg = "Should Exit in the text")
        self.assertEqual("THE" in z, False, msg="should not exit")    # case sensitive data
        self.assertEqual("The" in z, False, msg ="should not exit")

        z = x.add_file("test_same.txt")   # containing 10 same words with punctuation
        self.assertEqual(z["hello"], 10, msg="should be equal to the 10 according to the text")
        self.assertEqual("hello." in z, False, msg = "Should be False")

    def  test_rarity(self):
        """

        Unit test function to test the rarity function of the Task06
        """
        x = Task06.Freq()

        # Checking for the file
        with self.assertRaises(FileNotFoundError) as context:
            z = x.add_file("de.txt")

        # Checking the basic Function
        z = x.add_file("demo_small.txt")

        self.assertEqual(x.rarity("b"), 0, msg = "should be Equal")
        self.assertEqual(x.rarity("?"), 3, msg= "should be misspelling")
        # There is no "B" in the file but same as "b" because of the lower case
        self.assertEqual(x.rarity("B"),0, msg = "should be same as small alphabates")

        # Creating the database and searching through it
        z = x.add_file("PrideAndPrejudice.txt")
        z = x.add_file("frankenstein.txt")
        max_count  = x.max_count
        max_word   = x.max_word_appear
        self.assertEqual(x.rarity(x.max_word_appear), 0, msg="should be Equal to common")
        self.assertEqual(x.rarity("?"), 3, msg= "Should be no punctuation")
        word_count = z["frankenstein"]
        if word_count >= max_count / 100:
            retVal = 0
        elif word_count < max_count / 1000:
            retVal = 2
        else:
            retVal = 1
        self.assertEqual(x.rarity("frankenstein"), retVal, msg = "should be equal to the computed value")





if __name__ == '__main__':
    unittest.main()

# x["a"] = 1
# x["b"] = 2
# x["c"] = 3
# x["d"] = 4
# x["g"] = 5
#
# print(x.statistics())
