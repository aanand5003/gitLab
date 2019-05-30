from Task02_03 import load_dictionary
from Task03 import HashTable
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "24/05/2019"
"""


def test_load_dictionary():
    """
    Test the value the function of the load_dictionary
    @complexity: The best and the worst case is O(n) where n is the length of the number of lines in the text file.
    """

    filename = "error.txt"
    x = HashTable(2,1)
    try:
         return_value = load_dictionary(x, filename)
         print("Should have return error because there is no file name having " + filename +" in the folder")

    except:
          True

    filename = "two_words.txt"
    return_value = load_dictionary(x, filename)
    assert (return_value.array[1][1] == 1), "should be equal to the assign value = 1 but the value is" + str(return_value[1][1])
    assert(return_value.array[0][0] == "b"), "should be assign value b at location 1 but the value is " + return_value[0][0]

    filename = "demo.txt"
    x = HashTable(3, 7)
    return_value = load_dictionary(x, filename)
    assert (return_value["hello"] == 1), "Should be equals to the assign value = 1 but the value is " + return_value["hello"]

    f = open(filename, "r")  # open file to be read
    for i in f:
        i = i.strip()
        assert (x.__contains__(i)), "Should contains all values of the Text as a key"

    f.close()  # closing the file





def main():
    try:
        print ("Testing load_dictionary")
        test_load_dictionary()

    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()