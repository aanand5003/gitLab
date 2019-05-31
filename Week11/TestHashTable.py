#!/usr/bin/env python3
"""
:author: Graeme Gange
:updated by: Shourya Raj
"""
import math
import unittest
import Task01
import Task03

class TestHashTable(unittest.TestCase):
  def test_init(self):
    x = Task01.HashTable()
    y = Task01.HashTable(10)
    z = Task01.HashTable(800, 2398)

  def test_hash(self):
    x = Task01.HashTable(1024, 1)

    for (key, expect) in [("", 0),
                          ("abcdef", 597),
                          ("defabc", 597)]:
        self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 1 and key {key}.")

    x = Task01.HashTable(1024, 17)
    for (key, expect) in [("", 0),
                          ("abcdef", 389),
                          ("defabc", 309)]:
        self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 17 and key {key}.")

  # The tests for __contains__ and __getitem__ use __setitem__, so we don't make any assumptions
  # about the underlying array representation. Remember to define your own tests for __setitem__
  # (and rehash)
  def test_contains(self):
    x = Task01.HashTable(1024, 1)

    self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

    x["abcdef"] = 18
    x["definitely a string"] = None
    x["abdcef"] = "abcdef"
    
    for key in ["abcdef", "definitely a string", "abdcef"]:
      self.assertTrue(key in x, f"False negative in __contains__ for key {key}")

    self.assertFalse("defabc" in x, "False positive due to collision.")

  def test_getitem(self):
    x = Task01.HashTable(1024, 1)
    x = Task01.HashTable(1024, 1)

    with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
      elt = x["abcdef"]
      
    x["abcdef"] = 18
    x["definitely a string"] = None

    self.assertEqual(x["abcdef"], 18, msg = "Read after write failed.")
    self.assertEqual(x["definitely a string"], None, "Failed to retrieve written None.")

    x["abdcef"] = 22

    self.assertEqual(x["abcdef"], 18, msg = "Key overwritten by colliding value.")
    self.assertEqual(x["abdcef"], 22, msg = "Failed to write colliding value.")

    with self.assertRaises(KeyError, msg="False positive from colliding key."):
      elt = x["defabc"]

  def test_setitem(self):
    x = Task01.HashTable(10, 1)
    x["aaa"] = 100

    self.assertEqual(x["aaa"], 100, msg = "It should set value equals to 100")  # Checking the set value
    x["aaa"]  = 101
    self.assertEqual(x["aaa"], 101, msg = "It should change the value from 100 to 101 ")

    y = Task01.HashTable(5)
    y["a"] = "value0"
    y["b"] = "value1"
    y["f"] = "collision"   # value for the collision with the a
    # Using hash values a = 97 and 97 % 5 = 2 --- array location
    self.assertEqual(y.array[2][1], "value0", msg= "It should equals to the 'value2' ")
    self.assertEqual((y.array[3][1]), "value1", msg = "It should be equals to the 'value3'")
    self.assertEqual((y.array[4][1]), "collision", msg = "Collison value should be come after the"
                                                         " value1 because of linear probing")

  def test_rehash(self):
    x = Task01.HashTable(1)
    x["a"] = "value1"
    x["b"] = "value2"
    x["c"] = "value3"
    self.assertEqual(x.table_capacity, x.primes[0], msg = "It should increase the size by the prime value 3")
    self.assertEqual(x.array[1][1], "value1", msg= "After rehasing the value postion should be different " )
    self.assertRaises(Exception, msg= " Should have raised error")

    x = Task01.HashTable(1)
    for i in range(1001):
      x[str(i)] = i
      self.assertEqual(x.table_capacity % 2 == 0, False, msg= "It should be prime number every time." )

    self.assertEqual(x[str(1000)], 1000, msg = "It should be equals to the 1000")


  def test_statistics(self):
    x = Task03.HashTable(1)
    x["a"] = "value1"
    x["b"] = "value2"
    x["c"] = "value3"
    return_value = x.statistics()
    self.assertEqual(return_value[3], 1, msg = "It should be equals to the 1 but the rehash value is " +
                                              str(return_value[3]))
    x = Task03.HashTable(3, 1)
    x["a"] = "value1"
    x["d"] = "value2"  # collision with the a hash
    x["g"] = "value3"  # collision with the a hash
    return_value = x.statistics()
    self.assertEqual(return_value[0], 2, msg="Collision count is not working properly" ) # collision count
    self.assertEqual(return_value[1], 3, msg= "Probe count is not working properly")     # probe total
    self.assertEqual(return_value[2], 2, msg= "Probe Max is not calculating properly" )  # Probe Max

    x = Task03.HashTable(3)
    for i in range(1001):
      key = str(i)
      x[key] = 100
    self.assertEqual(x.table_capacity, 1931, msg= "Rehasing is not working properly")  # checking rehashing value

if __name__ == '__main__':
  unittest.main()
