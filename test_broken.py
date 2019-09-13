from sum import get_sum
from random import *

def test_sum():
    for i in range(1000):
        first = randint(-1000, 1000)
        second =  randint(-1000, 1000)
        assert(get_sum(first, second) == (first + first))

      
