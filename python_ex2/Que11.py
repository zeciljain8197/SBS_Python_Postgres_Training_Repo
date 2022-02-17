x = ['z', 'e', 'c', 'i', 'l']
y = {'j', 'a', 'i', 'n'}
z = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)

r = x
s = y
t = z
print(x)
print(y)
print(z)
print(r)
print(s)
print(t)

x.extend('The Great')
print(x)
print(r)

y.remove('j')
print(y)
print(s)

z.pop(1)
print(z)
print(t)

''' 
Performed various functions on the list , set and dictionaries to show that 
the changes are reflected in both the variables referring to those 
set, list and dicts.
'''

