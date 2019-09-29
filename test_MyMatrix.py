some_list = [[1, 2, 3], [4, 5, 6]]
m = MyMatrix(some_list)
empty_m = MyMatrix([])
def test_repr():
    assert(__repr__(m) == '1 2 3 /n4 5 6 /n')

def test_size():
    assert(size(m) == (3, 2))
    assert(empty_m.size() == 0)

def test_flip_left_right():
    m.flip_left_right()
    assert(size(m) == (3, 2))
    assert(m.get_data() == [[3 ,2, 1], [6, 5, 4]])
    assert(empty_m.flip_left_right().get_data() == [])
    

def test_flipped_left_right():
    m2 = m.flipped_left_right()
    m3 = empty_m.flipped_left_right()
    assert(size(m2) == (3, 2))
    assert(m2.get_data() == [[3 ,2, 1], [6, 5, 4]])
    assert(m.get_data() == some_list)
    assert(m3.get_data() == [])
    assert(empty_m.get_data() == [])

def test_flip_up_down():
    m.flip_up_down()
    assert(size(m) == (3, 2))
    assert(m.get_data() == [[4, 5, 6], [1, 2, 3]])
    assert(empty_m.flip_up_down().get_data() == [])

def test_flipped_up_down():
    m2 = m.flipped_up_down()
    assert(size(m2) == (3, 2))
    assert(m2.get_data() == [[4, 5, 6], [1, 2, 3]])
    assert(m.get_data() == some_list)
    assert(empty_m.flipped_up_down().get_data() == [])
    assert(empty_m.get_data() == [])

def test_transpose():
    m.transpose()
    assert(size(m) == (2, 3))
    assert(m.get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(empty_m.transpose().get_data() == [])

def test_transposed():
    m2 = m.transposed()
    assert(size(m) == (2, 3))
    assert(m2.get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(m.get_data() == some_list)
    assert(empty_m.transposed().get_data() == [])
    assert(empty_m.get_data() == [])

some_list2 = [[0, 9, 8], [7, 6, 5]]
m2 = MyMatrix(some_list2)

def test_add():
    assert((m + m2).get_data() == [[1, 11, 11], [11, 11, 11]])
    assert((empty_m + m2).get_data() == some_list2)
    assert((empty_m + m).get_data() == some_list)
    assert(m.get_data() == some_list)
    assert(m2.get_data() == some_list2)
    assert(empty_m.get_data() == [])

def test_sub():
    assert((m - m2).get_data() == [[1, -7, -5], [-3, -1, 1]])
    assert((m - empty_m).get_data() == some_list)
    assert((m2 - empty_m).get_data() == some_list2)
    assert(m.get.data() == some_list)
    assert(m.get.data() == some_list2)
    assert(empty_m.get_data() == [])


    
def test_iadd():
    m += empty_m
    m2 += empty_m
    assert(m.get_data() == some_list)
    assert(m2.get_data() == some_list2)
    m += m2
    assert(m.get_data() == [[1, 11, 11], [11, 11, 11]])
    assert(m.get.data2() == some_list2)
    assert(empty_m.get_data() == [])

    
def test_isub():
    m -= empty_m
    m2 -= empty_m
    assert((m).get_data() == some_list)
    assert((m2).get_data() == some_list2)
    m -= m2
    assert(m.get_data() == [[1, -7, -5], [-3, -1, 1]])
    assert(m.get.data2() == some_list2)
    assert(empty_m.get_data() == [])