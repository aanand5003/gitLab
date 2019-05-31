import math
import unittest
import Task08


class TestTask8(unittest.TestCase):
    def test_Delete(self):
        """
        Unit Testing for the Load Dictionary Function

        """
        x = Task08.HashTable(10, 2)
        x[str(3)] = 1
        x[str(4)] = 2
        x[str(5)] = 3
        x.__delete__(str(3))
        self.assertEqual(x.array[x.hash(str(3))], None, msg="1 should be at Oth position")

        x = Task08.HashTable(5)
        x["3"] = 1
        x["4"] = 2
        x["5"] = 3
        x["8"] = 6  # collision with the 3

        # [None,3,4,5,8] stored like this due to the hash_value
        self.assertEqual(x.array[1][1], 1, msg="1 should be at Oth position")
        self.assertEqual(x.array[2][1], 2, msg="2 should be at 1st position")
        self.assertEqual(x.array[3][1], 3, msg="3 should be at 2nd position")

        x.__delete__("3")

        # [None,8,4,6,"None"]  # 8 would come back here

        self.assertEqual("3" in x, False, msg="should be deleted but it did not")
        self.assertEqual(x.array[1][1], 6, msg="6 should be in the second position after reinserting")
        self.assertEqual(x.array[2][1], 2, msg="2 should be in the third position after reinserting")
        self.assertEqual(x.array[3][1], 3, msg = "3 should not have been effected by the delete")
        #so now after deleting it looks like
        #[b,k,l,None,None,g,a]

        x[str(3)] = 1
        
        self.assertEqual("3" in x, True, msg= "3 should be there in the HasTable")
        self.assertEqual(x.array[4][0], "3", msg="should be equals to the 3")
        self.assertEqual(x.array[4][1], 1, msg =" should be equals to 1")

if __name__ == '__main__':
    unittest.main()

# add test for setitem and rehash now
