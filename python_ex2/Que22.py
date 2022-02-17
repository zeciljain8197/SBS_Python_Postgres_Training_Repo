l = [('a', 1), ('b', 2), ('c', 3)]
t = (('d', 1), ('e', 2), ('f', 3))
s = {('g', 1), ('h', 2), ('i', 3)}
dict1 = {'j': 1, 'k': 2, 'l': 3}

res1 = list(t)
print(res1)
res2 = list(s)
print(res2)
res3 = list(dict1.items())

res4 = tuple(l)
print(res4)
res5 = tuple(s)
print(res5)
res6 = tuple(dict1)
print(res6)

res7 = set(l)
print(res7)
res8 = set(t)
print(res8)
res9 = set(dict1)
print(res9)

res10 = dict(l)
print(res10)
res11 = dict(t)
print(res11)
res12 = dict(s)
print(res12)
