from Task01 import *

def test_len():
    """
     Test function to test len method of the ListADT
     @post: Works without any error and exception if method len working fine
     @complexity: The best and worst case is  O(1)
     """
    x = ListADT()
    assert len(x) == 0, "Length should be 0 but is " + str(len(x))
    x.insert(0, 2)
    assert len(x) == 1, "Length should be 1 but is " + str(len(x))
    x.unsafe_set_array([1,2,3,3,4,5,5,6,7,6,8,None,None],11)
    assert len(x) == 11,"Length should be 11 but is" + str(len(x))

def test_str():
    """
       Test function to test str method of the ListADT
       @post: Works without any error and exception if method str working fine
       @complexity: The best O(1) and worst case is  O(M) where M is the length of the string
    """
    x = ListADT()
    assert str(x) == "", "Should be empty string but it is" + str(x)
    x.insert(0, 2)
    assert str(x) == "2\n", "Should be a 2 string but it is" + str(x)
    x.unsafe_set_array([1, 2, 3, None, None], 3)
    assert str(x) == "1\n2\n3\n", "Should be a 1 2 3 string but it is" + str(x)

def test_contains():
    """

       Test function to test contain method of the ListADT
       @post: Works without any error and exception if method contains working fine
       @complexity: The best and the worst case O(n)
    """
    x = ListADT()
    assert (2 in x) == False, "Should be False as x is empty but it is" + str(x)
    x.insert(0, 2)
    assert (2 in x), "Should be True as x=[2] but it is" + str(x)
    x.unsafe_set_array([4, 2, 3, None, None], 3)
    assert (3 in x), "Should be True as x=[4,2,3] but it is" + str(x)

def test_getitem():
    """

    Test function to test getitem method of the ListADT
    @post: Works without any error and exception if method getitem working correctly
    @complexity: The best and worst case O(1)
    """
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
    """

    Test function to test setitem method of the ListADT
    @post: Works without any error and exception if method setitem works correctly
    @complexity: The best and the worst case O(1)
    """
    x = ListADT()
    x.unsafe_set_array([4,3,5, None, None], 3)
    x[0] = 10
    x[1] = 20
    x[2] = 30
    assert (x[0] == 10), "Should be 10 but it is" + str(x[0])
    assert (x[1] == 20), "Should be 20 but it is" + str(x[1])
    assert (x[2] == 30), "Should be 30 but it is" + str(x[2])
    try:
        x[7] = 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_eq():
    """

    Test function to test __eq__ method of the ListADT
    @post: Works without any error and exception if method __eq__ works correctly
    @complexity: The best(1) and the worst case is 0(M) where M is the length of the string
    """
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
    """
    Test function to test insert method of the ListADT
    @post: Works without any error and exception if method insert works correctly
    @complexity: The worst case is O(1) and worst case O(length)
    """
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
    try:
        x.insert(1, 2)
    except:
        True
    x.unsafe_set_array([None,None,None], 1)
    try:
        x.insert(0,2)
    except:
        True
def test_delete():
    """
    Test function to test delete method of the ListADT
    @post: Works without any error and exception if method delete works correctly
    @complexity:  : The complexity best and worst case: O(length)
    """
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
    y = ListADT(100)
    capacity_y = len(y.the_array)
    for i in range(10):
        y.append(0)
    new_capacity_y = len(y.the_array)

    assert (capacity_y > new_capacity_y), "Should be True but new capacity= " + str(
                                          new_capacity_y) + " Old capacity is  +" + str(capacity_y)

    assert (new_capacity_y == 35 ), "Should be True but new capacity=  " + str(new_capacity_y)

def test_append():
    """
    Test function to test append method of the ListADT
    @post: Works without any error and exception if method append works correctly
    @complexity:  : The complexity best O(length) and worst case: O(length^2)
    """
    x = ListADT()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = ListADT()
    y.unsafe_set_array([1, 2, 3, 5, 6, 7, None, None], 6)
    try:
       x.append(9)
    except IndexError:
        True
    assert len(x) == 6, "Should be True but length of the array= " + str(len(x))
    assert x[(len(x)-1)] == 9, "Should be True but the last element is" + str(x[(len(x))])
    x = ListADT(300)
    capacity = len(x.the_array)
    for i in range(15):
        x.append(10)
    new_capacity = len(x.the_array)
    assert (capacity != new_capacity), "Should be True but new capacity= " + str(
                                        new_capacity) + " Old capacity is  +" + str(capacity)
    y = ListADT(10)
    capacity_y = len(y.the_array)
    for i in range(36):
        y.append(0)
    new_capacity_y = len(y.the_array)

    assert (capacity_y < new_capacity_y), "Should 1be True but new capacity= " + str(
                                          new_capacity_y) + " Old capacity is  +" + str(capacity_y)
    assert(new_capacity_y == round(35*1.6)),"Should be True but new capcaity= " + str(new_capacity_y)
    for i in range(36):
        y.append(0)
    new_capacity_y = len(y.the_array)
    assert (new_capacity_y == round(35 * 1.6 * 1.6)), "Should be True but new capcaity= " + str(new_capacity_y)



def test_resize():
    """
    Test the resize Method of the Task02 ListADT
    @post: Works without any error and exception if method resize works correctly
    @complexity:  : The best and the Worst case is O(n)
    """
    x = ListADT()
    size_x = 10
    array_x = [0]*size_x

    x.unsafe_set_array(array_x, 10)
    x.append(10)
    x.append(11)
    assert (x[10] == 10 and x[11] == 11), "Should be Value at x[10] is 10 and x[11] = 11 but is " +str(x[10]) +"and"+ str(x[11]) + "respectively"
    y = ListADT()
    size_y = 90
    array_y = [0] * size_y
    y.unsafe_set_array(array_y, 10)
    y.append(10)
    y.append(11)
    assert(x == y), " array 'x' should be equals to the array 'y' "

    y = ListADT(10)
    capacity_y = len(y.the_array)
    for i in range(36):
        y.append(0)
    new_capacity_y = len(y.the_array)

    assert (capacity_y < new_capacity_y), "Should 1be True but new capacity= " + str(
                                          new_capacity_y) + " Old capacity is  +" + str(capacity_y)




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
        print("Testing append")
        test_append()
        print("Testing resize")
        test_resize()

    except Exception as e:
        print("Error, unexpected exception: ", e)

if __name__ == '__main__':
    main()
