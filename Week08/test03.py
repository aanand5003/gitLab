from task03 import *


def test_task():
    list = read_text_file("story.txt")
    assert len(list) != None, "Should be true but length of the list is None"
    try:
        list[0]
    except:
        True
    f = open("story.txt", "r")
    line = f.readline()
    i = 0
    while line:
        assert list[i] == line, " Should be true but the value at the list index = " + str(i) + " should be " + " line"

        line = f.readline()
        i += 1
    f.close()

    f.close()


def main():
    try:
        print ("Testing the test_task")
        test_task()
    except Exception as e:
        print("Error, unexpected exception: ", e)


if __name__ == '__main__':
    main()
