from random import randint
from random import seed
from random import random
import time

def quicksort(array): 

    if len(array) <= 1:
        
        return array

    less = []
    equal = []
    great = []

    
    pivot = randint(0, len(array) - 1)


    for number in array:
        
        if number < array[pivot]:
            
            less.append(number)
            
        elif number == array[pivot]:
            
            equal.append(number)
            
        else:
            
            great.append(number)

    return quicksort(less) + equal + quicksort(great)


##Generate Random values to test quicksort algorithm

seed(1)

test1_array = []
start_time1 = time.time()

for _ in range(50):
	value = test1_array.append(randint(0, 1000))


print(quicksort(test1_array))
print(time.time() - start_time1)


seed(1)

test2_array = []
start_time2 = time.time()

for _ in range(50):
	value = test2_array.append(randint(0, 1000))


print(quicksort(test2_array))
print(time.time() - start_time2)

seed(1)

test3_array = []
start_time3 = time.time()

for _ in range(50):
	value = test3_array.append(randint(0, 1000))

print(quicksort(test3_array))
print(time.time() - start_time3)


seed(1)

test4_array = []
start_time4 = time.time()

for _ in range(50):
	value = test4_array.append(randint(0, 1000))

print(quicksort(test4_array))
print(time.time() - start_time4)


seed(1)

test5_array = []
start_time5 = time.time()

for _ in range(50):
	value = test5_array.append(randint(0, 1000))

print(quicksort(test5_array))
print(time.time() - start_time5)
