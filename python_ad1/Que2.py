import random


def add_func(func):
    def var():
        x = func()
        return x+10

    return var


def sqr_func(func):
    def var():
        x = func()
        return x**2

    return var


@add_func
@sqr_func
def func1():
    a = random.randrange(1, 100)
    print(a)
    return a

print(func1())
