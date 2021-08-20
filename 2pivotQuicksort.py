from random import randint
from random import seed
from random import random
import time


def dual_pivot_sort(array):
    n = len(array)
    if n<= 1:
        return array
    elif n == 2:
        return sorted(array)
    pivot1, pivot2 = sorted([array.pop(0), array.pop(0)])
    a= []
    b = []
    c = []
    for element in array:
        if element < pivot1:
            a.append(element)
        elif pivot1 <= element and element < pivot2:
            b.append(element)
        else:
            c.append(element)
    return dual_pivot_sort(a) + [pivot1] + dual_pivot_sort(b) + [pivot2] + dual_pivot_sort(c)
    



##Generate Random values to test quicksort algorithm

seed(1)

test1_array = []
start_time1 = time.time()

for _ in range(50):
	value = test1_array.append(randint(0, 1000))


print(dual_pivot_sort(test1_array))
print(time.time() - start_time1)


seed(1)

test2_array = []
start_time2 = time.time()

for _ in range(50):
	value = test2_array.append(randint(0, 1000))


print(dual_pivot_sort(test2_array))
print(time.time() - start_time2)

seed(1)

test3_array = []
start_time3 = time.time()

for _ in range(50):
	value = test3_array.append(randint(0, 1000))

print(dual_pivot_sort(test3_array))
print(time.time() - start_time3)


seed(1)

test4_array = []
start_time4 = time.time()

for _ in range(50):
	value = test4_array.append(randint(0, 1000))

print(dual_pivot_sort(test4_array))
print(time.time() - start_time4)


seed(1)

test5_array = []
start_time5 = time.time()

for _ in range(50):
	value = test5_array.append(randint(0, 1000))

print(dual_pivot_sort(test5_array))
print(time.time() - start_time5)
