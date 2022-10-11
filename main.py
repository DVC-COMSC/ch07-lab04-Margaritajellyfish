
# ******************************
# Make your Code
# ******************************
import random

numbers1 = []
numbers2 = []
result = []
for i in range(10):
	numbers1.append(random.randint(0,100))
	numbers2.append(random.randint(0,100))
print (numbers1)
print (numbers2)
for j in range(10):
	w = numbers1[j] + numbers2[j]
	result.append(w) 
print(result)