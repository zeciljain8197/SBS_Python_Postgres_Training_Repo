import random

lst = []
i = 0
while i < 4:
    n = random.randrange(1, 101)
    if n not in lst:
        lst.append(n)
        i += 1

print(lst)
