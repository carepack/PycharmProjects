import random

ran_num1 = random.randint(5,20)
ran_num2 = random.randint(5,20)

# random.sample generates no duplicates
a = random.sample(range(100), ran_num1)
b = random.sample(range(100), ran_num2)

c = [num for num in a if num in b]

print()
print(ran_num1)
print(ran_num2)
print()
print(a)
print(b)
print()
print(c)


