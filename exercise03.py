# 13.11.2019
# check for gt / lt. single and list output

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
c=[]

for element in a:
    if element < 5:
        print(element)
        b.append(element)

print(b)

in_num = int(input("Tell me a number: "))

for element in a:
    if element < in_num:
        print(element)
        c.append(element)

print(c)