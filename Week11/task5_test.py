import Task05

"""
:author: Graeme Gange
:updated by: Shourya Raj
"""
import math
import unittest

class TestHashTable(unittest.TestCase):
    def test_init(self):
        x = Task05.HashTable()
        y = Task05.HashTable(10)
        z = Task05.HashTable(800, 2398)

    def test_hash(self):
        x = Task05.HashTable(1024, 1)

        for (key, expect) in [("", 0),
                              ("abcdef", 597),
                              ("defabc", 597)]:
            self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 1 and key {key}.")

        x = Task05.HashTable(1024, 17)
        for (key, expect) in [("", 0),
                              ("abcdef", 389),
                              ("defabc", 309)]:
            self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 17 and key {key}.")


    def test_contains(self):
        x = Task05.HashTable(1024, 1)

        self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

        x["abcdef"] = 18
        x["definitely a string"] = None
        x["abdcef"] = "abcdef"

        for key in ["abcdef", "definitely a string", "abdcef"]:
            self.assertTrue(key in x, f"False negative in __contains__ for key {key}")

        self.assertFalse("defabc" in x, "False positive due to collision.")

    def test_getitem(self):
        x = Task05.HashTable(1024, 1)
        x = Task05.HashTable(1024, 1)

        with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
            elt = x["abcdef"]

        x["abcdef"] = 18
        x["definitely a string"] = None

        self.assertEqual(x["abcdef"], 18, msg="Read after write failed.")
        self.assertEqual(x["definitely a string"], None, "Failed to retrieve written None.")

        x["abdcef"] = 22

        self.assertEqual(x["abcdef"], 18, msg="Key overwritten by colliding value.")
        self.assertEqual(x["abdcef"], 22, msg="Failed to write colliding value.")

        with self.assertRaises(KeyError, msg="False positive from colliding key."):
            elt = x["defabc"]

    def test_setitem(self):
        x = Task05.HashTable(10, 1)
        x["aaa"] = 100

        self.assertEqual(x["aaa"], 100, msg="It should set value equals to 100")  # Checking the set value
        x["aaa"] = 101
        self.assertEqual(x["aaa"], 101, msg="It should change the value from 100 to 101 ")

        y = Task05.HashTable(5)
        y["a"] = "value0"
        y["b"] = "value1"
        y["f"] = "collision"  # value for the collision with the a
        # Using hash values a = 97 and 97 % 5 = 2 --- array location
        self.assertEqual(y.array[2][0]["a"], "value0" , msg="It should equals to the 'value2' ")
        self.assertEqual((y.array[3][0]["b"]), "value1", msg="It should be equals to the 'value3'")
        self.assertEqual((y.array[2][0]["f"]), "collision", msg="Collison value should be come after the"
                                                           " value1 because of chain probing")

        y = Task05.HashTable(5)

        y["a"] = 1
        y["a"] = 2
        y["a"] = 3
        y["a"] = 4
        self.assertEqual("a" in y.array[2][0], True, msg="It should equals to the true ")
        self.assertEqual(y.array[2][0]["a"], 4, msg="It should equals to the true ")

        y = Task05.HashTable(1)
        y["a"] = 1
        y["b"] = 1
        y["c"] = 1
        y["d"] = 1
        y["e"] = 1
        y["f"] = 1
        self.assertEqual("a" in y.array[0][0], True, msg="It should equals to the true ")
        self.assertEqual("b" in y.array[0][0], True, msg="It should equals to the true ")
        self.assertEqual("c" in y.array[0][0], True, msg="It should equals to the true ")
        self.assertEqual("d" in y.array[0][0], True, msg="It should equals to the true ")
        self.assertEqual("e" in y.array[0][0], True, msg="It should equals to the true ")
        self.assertEqual("f" in y.array[0][0], True, msg="It should equals to the true ")




    def test_statistics(self):
        x = Task05.HashTable(3)
        x["a"] = "value1"
        x["b"] = "value2"
        x["c"] = "value3"
        return_value = x.statistics()
        self.assertEqual(return_value[0], 0, msg="It should be equals to the 1 but the rehash value is " +
                                                 str(return_value[0]))
        x = Task05.HashTable(3, 1)
        x["a"] = "value1"
        x["d"] = "value2"  # collision with the a hash
        x["g"] = "value3"  # collision with the a hash
        return_value = x.statistics()
        self.assertEqual(return_value[0], 2, msg="Collision count is not working properly")  # collision count
        self.assertEqual(return_value[1], 3, msg="Probe count is not working properly")  # probe total
        self.assertEqual(return_value[2], 2, msg="Probe Max is not calculating properly")  # Probe Max

        # x = Task05.HashTable(3)
        # for i in range(1000):
        #     key = str(i)
        #     x[key] = 100
        # self.assertEqual(x.table_capacity, 1931, msg="Rehasing is not working properly")  # checking rehashing value


if __name__ == '__main__':
    unittest.main()

# x["a"] = 1
# x["b"] = 2
# x["c"] = 3
# x["d"] = 4
# x["g"] = 5
#
# print(x.statistics())
