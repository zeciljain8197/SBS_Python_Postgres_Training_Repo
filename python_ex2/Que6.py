x = {1, 2, 3, 4, 5, 6, 7, 8}
y = {6, 7, 8, 9, 10, 11, 12, 13}

z = x
w = x.copy()
print(z)
print(w)

z.add(10)
print(z)
y.remove(13)
print(y)
y.discard(13)
print(y)
print(z)
print(w)
res = x.pop()
print(x)
res1 = y.pop()
print(y)

y.update(x)
print(y)

res2 = x.union(y)
print(res2)
res3 = x.intersection(y)
print(res3)
res4 = y.difference(x)
print(res4)
res5 = x.symmetric_difference(y)
print(res5)
print(x.issubset(y))
print(y.issuperset(x))
print(x.isdisjoint(y))