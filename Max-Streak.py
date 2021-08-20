import random
import math

from collections import Counter
from collections import OrderedDict
from matplotlib import pyplot as plt
import numpy as np

global_number = 8

values = []

label_range = tuple(range(1,global_number  + 1))



def randint(number):


    count = 0
    #counter = math.ceil(math.log(number)/math.log(2)) - 1
    counter =  int(math.floor(math.log(number) / math.log(2)))
    #counter = int(math.ceil(math.sqrt(number)))- 1
    
    for j in range(counter, -1, -1):
        
        count += ((2 ** j) * int(random.getrandbits(1)))



    if ((number * count) / (2 ** counter) % number == 0):
        return number
    else:
        return (number * count) / (2 ** counter) % number
        





for j in range(1000000):
        
        values.append(randint(global_number))


print(np.average(values))


def randint(array):

	streak = 0

	max_streak = 0

	for k in range(len(array) - 1):

		if (array[k] == array[k+1]):
			streak += 1
		elif (array[k] != array[k+1]):
			max_streak = max(streak + 1, max_streak)
			streak = 0
	return max_streak


print(randint(values))

labels, values = zip(*Counter(values).items())
data = dict(zip(labels,values))
for j in label_range:
        if j not in data:
            data[j] = 0
sorted_data= OrderedDict(sorted(data.items()))


plt.bar(range(len(sorted_data)), list(sorted_data.values()), align='center')
plt.xticks(range(len(sorted_data)), list(sorted_data.keys()))
plt.show()
