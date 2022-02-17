# Take 10 numbers in a list(array) and print only first 3 numbers using loop.

lst = []
lst1 = []
for i in range(10):
    x = int(input())
    lst.append(x)
    if i < 3:
        lst1.append(lst[i])
    else:
        continue
print(lst1)

