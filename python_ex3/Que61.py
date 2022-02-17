import random

lst = []
for i in range(1, 11): lst.append(i)
cb = list(map(lambda a: a * a * a, lst))
print(cb)
