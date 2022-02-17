l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
s = {21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for i in l:
    print(i)
for i in t:
    print(i)
for i in s:
    print(i)
for i in d.items():
    print(i)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i, j in d.items():
    print(i, j)
