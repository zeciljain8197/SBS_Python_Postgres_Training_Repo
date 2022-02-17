import random
count = []


def rr():
    x = random.randrange(101)
    if x not in count:
        count.append(x)
        print(x, end=" ")
    else:
        rr()


for i in range(10):
    rr()
