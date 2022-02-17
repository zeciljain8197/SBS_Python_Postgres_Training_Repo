import random

lst1 = []
lst2 = []
for i in range(1, 11): lst1.append(random.randrange(1, 100)), lst2.append(random.randrange(1, 100))
print(lst1)
print(lst2)
lst = list(map(lambda a, b: a * b, lst1, lst2))
print(lst)
