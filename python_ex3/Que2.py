x = {'a': 20}
y = [30]

try:
    print(y[1])         # IndexError
    print(x[a])         # KeyError
    print(y[0]/0)       # ZeroDivisionError
    print(z)            # NameError
    print('a' + 19)     # TypeError

except IndexError as i:
    print(i)
except KeyError as k:
    print(k)
except ZeroDivisionError as zd:
    print(zd)
except NameError as n:
    print(n)
except TypeError as t:
    print(t)
