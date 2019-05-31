"""
@shoourya Raj
@28963555
@
"""

import Task06

"""
:author: Shourya Raj
"""
import math

import unittest

class FreqTest(unittest.TestCase):


    def test_add_file(self):
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
        self.assertEqual("THE" in z, False, msg="should not exit")
        self.assertEqual("The" in z, False, msg ="should not exit")

        z = x.add_file("test_same.txt")   # containing 10 same words with punctuation
        self.assertEqual(z["hello"], 10, msg="should be equal to the 10 according to the text")
        self.assertEqual("hello." in z, False, msg = "Should be False")

    def  test_rarity(self):
        x = Task06.Freq()
        z = x.add_file("demo_small.txt")

        self.assertEqual(x.rarity("b"), 0, msg = "shoulb be Equal")
        self.assertEqual(x.rarity("?"), 3, msg= "should be misspelling")
        # there is no "B" in the file but same as "b"
        self.assertEqual(x.rarity("B"),0, msg = "should be same as small alphabates")





if __name__ == '__main__':
    unittest.main()

# x["a"] = 1
# x["b"] = 2
# x["c"] = 3
# x["d"] = 4
# x["g"] = 5
#
# print(x.statistics())
