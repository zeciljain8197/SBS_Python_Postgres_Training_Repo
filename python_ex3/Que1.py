x = {'a': 20}
y = [30]

print(y[1])         # IndexError
print(x[a])         # KeyError
print(y[0]/0)       # ZeroDivisionError
print(y[0)          # SyntaxError
print(z)            # NameError
print('a' + 19)     # TypeError