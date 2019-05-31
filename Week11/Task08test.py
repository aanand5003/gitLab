import math
import unittest
import Task08


class TestTask8(unittest.TestCase):
    def test_load_dictionary(self):
        x=Task08.HashTable(5)
        x["1"] = 1
        x["2"] = 2
        x["3"] = 3
        x["4"] = 4

         # [1,2,3,4, "None"] stored like this due to the hash_value
        self.assertEqual(x.array[1][0], "1", msg="1 should be at Oth position")
        self.assertEqual(x.array[2][0], "2", msg="2 should be at 1st position")
        self.assertEqual(x.array[3][0], "3", msg="3 should be at 2nd position")

        x.__delete__("c")
        #
        # for i in range(7):
        #     if x.array[i] is None:
        #         print("ss")
        #     else:
        #         print(x.array[i][0])
        self.assertEqual("c" in x, False, msg="c should be deleted but it did not")
        self.assertEqual(x.array[1][0], "j", msg="j should be in the second position after reinserting")
        self.assertEqual(x.array[2][0], "k", msg="k should be in the third position after reinserting")
        self.assertEqual(x.array[5][0], "g", msg = "g should not have been effected by the delete")
        #so now after deleting it looks like
        #[b,k,l,None,None,g,a]



if __name__ == '__main__':
    unittest.main()

# add test for setitem and rehash now
