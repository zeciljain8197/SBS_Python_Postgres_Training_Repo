import random

lst = []
for i in range(1, 11): lst.append(random.randrange(0, 2))
print(lst)
if 1 in lst:
    if 0 in lst:
        print("Any")
    else:
        print("All")
else:
    print("None")

