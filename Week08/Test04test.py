from Task06 import*
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "10/05/2019"
"""

def delete_num_test():
    a = Editor()

    a.read_filename("own.txt")
    a.delete_num(-1)

    b = Editor()         # Testing with the negative number
    b.read_filename("own.txt")

    assert(a.text_lines[len(a.text_lines)- 1]  == b.text_lines[len(b.text_lines)-2]), "Should be equal but the delete function dosen't delete the element"

    # Testing to delete all element
    a.read_filename("story.txt")
    a.delete_num()

    assert(len(a.text_lines) == 0), "Should be equal to the zero but the line is equal to" + str(len(a.text_lines))

    b.read_filename("story.txt")
    try:
      b.delete_num(0)
      print("Should have raised an error because there is no zero line")
    except:
        True
def test_insert_num_string():
    # Test to check inserted string inserted in the correct order
    a = Editor()
    a.read_filename("own.txt")

    string = ListADT()
    string.append("1")
    string.append("2")
    string.append("3")
    string.append("4")
    a.insert_num_string(1,string)
    test = ["1","2","3"]
    for i in range(len(test)):
        assert(a.text_lines[i] == test[i]), "Should be equal to the postion of the test array but order is different"
    # testing with the negative index to check the to see the position
    a.read_filename("own.txt")
    stringList =ListADT()
    stringList.append("1")
    stringList.append("2")

    a.insert_num_string(-1,stringList)

    b= Editor()
    b.read_filename("own.txt")
    b.text_lines.append("1")
    b.text_lines.append("2")

    assert(a.text_lines == b.text_lines),"Should be equal but the value is not in the correct order"
    try:
        b.insert_num_string(0, stringList)
        print("Should Have raise error ")
    except:
        True


def main():
    try:
        print ("Testing delete_num_test")
        delete_num_test()
        print("Testing test_insert_num_string")
        test_insert_num_string()
    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()