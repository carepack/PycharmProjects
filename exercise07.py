# 13.11.2019
# lsit comprehension. collect even numbers in new list

import random

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [num for num in a if num % 2 == 0]
c = []
print(b)



for i in range(20):
    c.append(random.randrange(100))

d = [num for num in c if num % 2 == 0]
print(c)
print(d)