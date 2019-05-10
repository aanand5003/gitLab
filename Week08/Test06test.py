from Task06 import*
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "10/05/2019"
"""

def test_undo():
    a = Editor()

    # Checking that undo function for the insert

    b = ListADT()
    b.append("Test1")
    ca.read_filename("own.txt") = ListADT()
    c.append("Test2")
    a.insert_num_string(1,b)
    a.insert_num_string(1,c)  # inserting item at position 1
    a.undo()
    assert(a.text_lines[0] == "Test1"), "Should be equal to 1 but" + a.text_lines[1]+ "showing at  Test2"   # At line 1 means 0 position of the text_line
    # checking undo function to recover all deleted string.
    a.read_filename("story.txt")
    b = Editor()
    b.read_filename("story.txt")
    a.delete_num()
    a.undo()
    assert(a.text_lines == b.text_lines),"Should be equals to same list after the undo but it dosen't recoverd"

    #checking Undo function for the each deleted line
    a.read_filename("own.txt")
    c = ListADT()
    d = ListADT()
    c.append("Test2")
    c.append("Test3")
    
    a.insert_num_string(2, c)
    a.delete_num(2)
    a.undo()
    # Line is +1 from the array hence 2-1 =1 for the array
    assert(a.text_lines[1] == b.text_lines[1]),"Should be equals to same element but it haven't recover" + a.text_lines[1]

def main():
    try:
        print ("Testing undo")
        test_undo()
    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()