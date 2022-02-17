dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'd': 5, 'e': 6}

res = dict2.copy()
res.update(dict1)
print(res)
