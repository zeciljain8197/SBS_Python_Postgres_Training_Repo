import random

lst = []
for i in range(10):
    n = random.randrange(1, 100)
    lst.append(n)
    
print(lst)
print(max(lst))