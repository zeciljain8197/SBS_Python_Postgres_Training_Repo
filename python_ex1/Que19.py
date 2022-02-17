# Create a function which will take unlimited arguments both non keyword and
# keyword arguments. Add the values of all non keyword arguments and also the
# value of keyword arguments.

def func(*args, **kwargs):
    sum1 = 0
    sum2 = 0
    for arg in args:
        sum1 += arg

    values = kwargs.values()
    sum2 = sum(values)
    return sum1 + sum2


l1 = func(8, 9, 10, 12, a=2, b=13, c=7)
print(l1)
