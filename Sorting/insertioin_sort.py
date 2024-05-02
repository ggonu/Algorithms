# insertion sort

import random
from timeit import default_timer as timer

def test(x):
    for i in range(1, len(x) - 1):
        if x[i] > x[i - 1]: return True
    return False

def insertion_sort(x):
    for i in range(1, len(x) - 1):
        loc = i - 1
        new_item = x[i]
        while loc >= 0 and new_item < x[loc]:
            x[loc + 1] = x[loc]
            loc -= 1
        x[loc + 1] = new_item

x = random.sample(range(10000), 100)
start = timer()
insertion_sort(x)
print(timer() - start)
print(x)
print(test(x))
