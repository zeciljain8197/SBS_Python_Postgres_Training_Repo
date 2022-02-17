import random

lst = []
for i in range(1, 16): lst.append(random.randrange(1, 100))
print(lst)
print(sum(lst))