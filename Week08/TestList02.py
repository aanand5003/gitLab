from Task01 import *

def test_len():
    x = ListADT()
    assert len(x) == 0, "Length should be 0 but is " + str(len(x))
    x.insert(0, 2)
    assert len(x) == 1, "Length should be 1 but is " + str(len(x))
    x.unsafe_set_array([1,2,3,3,4,5,5,6,7,6,8,None,None],11)
    assert len(x) == 11,"Length should be 11 but is" + str(len(x))

def test_str():
    x = ListADT()
    assert str(x) == "", "Should be empty string but it is" + str(x)
    x.insert(0, 2)
    assert str(x) == "2\n", "Should be a 2 string but it is" + str(x)
    x.unsafe_set_array([1, 2, 3, None, None], 3)
    assert str(x) == "1\n2\n3\n", "Should be a 1 2 3 string but it is" + str(x)

def test_contains():
    x = ListADT()
    assert (2 in x) == False, "Should be False as x is empty but it is" + str(x)
    x.insert(0, 2)
    assert (2 in x), "Should be True as x=[2] but it is" + str(x)
    x.unsafe_set_array([4, 2, 3, None, None], 3)
    assert (3 in x), "Should be True as x=[4,2,3] but it is" + str(x)

def test_getitem():
    x = ListADT()
    x.unsafe_set_array([4,3,5,6, None, None], 4)
    assert (x[0] == 4), "Should be 4 but it is" + str(x[0])
    assert (x[1]== 3), "Should be 3 but it is" + str(x[1])
    assert (x[3] == 6), "Should be 6 but it is" + str(x[3])
    try:
        x[7] == 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_setitem():
    x = ListADT()
    x.unsafe_set_array([4,3,5, None, None], 3)
    x[0]=10
    x[1]=20
    x[2]=30
    assert (x[0] == 10), "Should be 10 but it is" + str(x[0])
    assert (x[1] == 20), "Should be 20 but it is" + str(x[1])
    assert (x[2] == 30), "Should be 30 but it is" + str(x[2])
    try:
        x[7] = 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_eq():
    x = ListADT()
    x.unsafe_set_array([4, 3, 5, None, None], 3)
    y = ListADT()
    y.unsafe_set_array([4, 3, 5, None, None], 3)
    z = ListADT()
    z.unsafe_set_array([4, 5, 3, None, None], 3)
    w = ListADT()
    w.unsafe_set_array([4, 5, None, None], 2)
    assert (x == y), "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    assert (x != z), "Should be False but it is" + "x="+ str(x) + "z=" + str(z)
    assert (x != w), "Should be False but it is" + "x="+ str(x) + "w=" + str(w)
    try:
        x[7] = 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_insert():
    x = ListADT()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = ListADT()
    y.unsafe_set_array([1, 2, 3, 5, 6, 7, None, None], 6)
    x.insert(2, 3)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    x.insert(0, 0)
    y.unsafe_set_array([0, 1, 2, 3, 5, 6, 7, None, None], 7)
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    try:
        x.insert(12, 2)
        print("Should have raised IndexError")
    except IndexError:
            True

def test_delete():
    x = ListADT()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = ListADT()
    y.unsafe_set_array([1, 2, 6, 7, None, None], 4)
    item = x.delete(2)
    assert (item == 5 and x == y), "Should be True but it is" + "item=" +str(item)+"x=" + str(x) + "y=" + str(y)
    item = x.delete(0)
    y.unsafe_set_array([2, 6, 7, None, None], 3)
    assert (item == 1 and x == y), "Should be True but it is" + "item=" + str(item) + "x=" + str(x) + "y=" + str(y)
    try:
        x.delete(12)
        print("Should have raised IndexError")
    except IndexError:
        True
def test_resize():
    x = ListADT()
    size_x = 10
    array_x = [0]*size_x

    x.unsafe_set_array(array_x, 10)
    try:
      x.append(10)
      x.append(11)
    except:
        True
    assert (x[10] == 10 and x[11] == 11), "Should be Value at x[10] is 10 and x[11] = 11 but is " +str(x[10]) +"and"+ str(x[11]) + "respectively"
    y = ListADT()
    size_y = 90
    array_y = [0] * size_y
    y.unsafe_set_array(array_y, 10)
    y.append(10)
    y.append(11)
    assert(x == y), " array 'x' should be equals to the array 'y' "
    try:
      x.insert(len(x), 12)
      x.insert((len(x), 13))
    except:
        True




    new_length = len(x)


def main():
    # Run the tests when the module is called from the command line
    ListADT.in_test_mode = True
    try:
        print("Testing length")
        test_len()
        print("Testing str")
        test_str()
        print("Testing contains")
        test_contains()
        print("Testing getitem")
        test_getitem()
        print("Testing setitem")
        test_setitem()
        print("Testing eq")
        test_eq()
        print("Testing insert")
        test_insert()
        print("Testing delete")
        test_delete()
        print("Testing resize")
        test_resize()

    except Exception as e:
        print("Error, unexpected exception: ", e)

if __name__ == '__main__':
    main()
