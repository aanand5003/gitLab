import math
import unittest
import Task08


class TestTask8(unittest.TestCase):
    def test_load_dictionary(self):
        x=Task08.HashTable(7)
        x["a"] = 1
        x["b"] = 2
        x["c"] = 3
        x["g"] = 6
        x["j"] = 4
        x["k"] = 5

        self.assertEqual(x.array[1][0], "c", msg="c should be in the second position of the hash table")
        self.assertEqual(x.array[2][0], "j", msg="j should be in the second position of the hash table but probed once to the third")
        self.assertEqual(x.array[3][0], "k", msg="k should be in the third position of the hash table but probed twice to fourth")
        # so the letters are in the following order in the array
        # [b,c,j,k,None,g,a]

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
