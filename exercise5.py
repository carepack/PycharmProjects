# 13.11.2019
# Überlagernde Liste und ermitteln von Übereinstimmungen
# Liste randomisert erstellen

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = []
e = []
f = []

for element in a:
        if element in b:
                if element not in c:
                        c.append(element)
print()
print(c)
print()

for i in range(15):
        d.append(random.randrange(20))
        e.append(random.randrange(20))
print(d)
print(e)

for element in d:
        if element in e:
                if element not in f:
                        f.append(element)
print()
print(f)
