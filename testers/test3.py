from sum import get_sum
from random import *

def test_sum():
    for i in range(1000):
        alphabet = "ABCDEFGHIKLMNOPQRSTVXYZ"
        first = choice(alphabet)
        second =  choice(alphabet)
        assert(get_sum(first, second) == (first + second))

      
