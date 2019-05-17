from Task05 import*
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "10/05/2019"
"""

def test_search_string():
    a = Editor()
    a.text_lines.append("Hello")
    a.text_lines.append("How are you?")
    a.text_lines.append("I am good")
    assert(a.search_string("Hello")[0] == 1), "Should be equal to 1 but 'Hello' showing at " + a.search_string("Hello")[0]
    a.read_filename("own.txt")
    a = Editor()
    a.text_lines.append("okay okay okay okay okay okay okay okay")
    assert(a.search_string("okay")[0] == 1), "Should be equal to 4 but showing at" + a.search_string("okay")[0]
    try:
        a.search_string()
        print("Should Print Error Because without string it can't search anything")
    except:
        True

def main():
    try:
        print ("Testing search_string")
        test_search_string()
    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()