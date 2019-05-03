from task03 import *


def test_task():
    """
    Test the read_text_file method of the task03 file
    @post: Works without any error and exception if method append works correctly
    @complexity: The best case and the worst case is O(length * M) where Length is length is
                 number of lines and M is the size of the string.
    """
    list = read_text_file("story.txt")
    assert len(list) != None, "Should be true but length of the list is None"
    f = open("story.txt", "r")
    line = f.readline()
    number_line = 0
    while line:
        line = f.readline()
        number_line += 1
    f.close()
    assert len(list) == number_line, " Should be True but the length of list =" + str(len(list))
    f = open("story.txt", "r")
    i = 0
    line = f.readline()
    while line:
        assert list[i] == line, " Should be true but the value at the list index = " + str(i) + " should be " + " line"

        line = f.readline()
        i += 1
    f.close()
    try:
        list[number_line+1]
        print("Should through an IndexError exception")
    except IndexError:
        True


def main():
    try:
        print ("Testing read_text_file")
        test_task()
    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()
