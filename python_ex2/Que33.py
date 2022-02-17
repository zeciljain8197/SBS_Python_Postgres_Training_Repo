l = [1, 2, 3, 4, 5, 6, 7]
w = l
t = (1, 2, 3, 4)
x = t
s = {1, 2, 3, 4, 5, 6}
y = s
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = dict1

if 10 not in l:
    print('Yes')
if 3 in l:
    print('Yes')
if l is w:
    print('True')
if l is not t:
    print('False')

if 10 not in t:
    print('Yes')
if 3 in t:
    print('Yes')
if t is x:
    print('True')
if t is not l:
    print('False')

if 10 not in s:
    print('Yes')
if 3 in s:
    print('Yes')
if s is y:
    print('True')
if s is not l:
    print('False')

if 'z' not in dict1:
    print('Yes')
if 'a' in dict1:
    print('Yes')
if dict1 is dict2:
    print('True')
if dict1 is not l:
    print('False')