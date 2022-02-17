import random

# passing values manually
lst1 = [2, 35, 65, 1, 23, 82, 23.2, 4, 54.1, -1]
lst1.sort()
print(lst1)

# Using in-built random class to get random values
lst2 = []
for _ in range(10):
    lst2.append(random.randrange(-100, 100))
print(lst2)
lst2.sort()
print(lst2)
