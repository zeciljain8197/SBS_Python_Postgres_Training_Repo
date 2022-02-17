# Create two functions. Call one function from another function.

def testfunc1(x, y):
    c = x + y
    return c


def testfunc2(a, b):
    return testfunc1(a, b)


print(testfunc2(8, 10))
