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
    a.menu
    a.read_filename("own.txt")
    b = ListADT()
    b.append("Test1")
    c = ListADT()
    c.append("Test2")
    a.insert_num_string(1,b)
    a.insert_num_string(1,c)  # inserting item at position 1
    a.undo()
    assert(a.text_lines[0] == "Test1"), "Should be equal to 1 but 'Hello' showing at " + a.search_string("Hello")[0]


def main():
    try:
        print ("Testing search_string")
        test_undo()
    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()