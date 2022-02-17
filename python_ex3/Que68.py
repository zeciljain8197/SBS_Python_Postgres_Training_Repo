import random

lst = []
for i in range(0, 25):
    lst.append(random.randrange(0, 100))
lst1 = []

while lst:
    minimum = lst[0]  # arbitrary number in list
    for x in lst:
        if x < minimum:
            minimum = x
    lst1.append(minimum)
    lst.remove(minimum)

print(lst1)
