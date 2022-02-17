import random

lst = []
for i in range(10): lst.append(random.randrange(1, 100))


def fil_ele_even(el):
    if el % 2 == 0:
        return True
    else:
        return False


def fil_ele_odd(el):
    if el % 2 != 0:
        return True
    else:
        return False


res = list(filter(fil_ele_even, lst))
print(res)
res1 = list(filter(fil_ele_odd, lst))
print(res1)
