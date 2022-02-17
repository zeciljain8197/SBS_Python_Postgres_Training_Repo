import random


def dec_func(func):
    def var():
        a = random.randrange(1, 11)
        b = random.randrange(1, 11)
        return func(a, b)

    return var


@dec_func
def add(a, b):
    print("For add:", a, b)
    print(a + b)


@dec_func
def sub(a, b):
    print("For sub:", a, b)
    print(a - b)


@dec_func
def mul(a, b):
    print("For mul:", a, b)
    print(a * b)


@dec_func
def div(a, b):
    print("For div:", a, b)
    print(a / b)


add()
sub()
mul()
div()
