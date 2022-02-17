# Perform overloading for constructors and methods defined in the class.

class Parent1:
    def __init__(self, a, b=0, c=0):
        if not b and not c:
            self.x = a
            print(a, b, c)

        else:
            self.x = a
            self.y = b
            self.z = c
            print(a, b, c)


class Parent2:

    def mul(self, a, b=0, c=0):
        if not b and not c:
            return a + b + c
        elif not b or not c:
            return a - b - c
        else:
            return a * b * c


o1 = Parent1(1)
o1 = Parent1(3, 8)
o1 = Parent1(3, 5, 8)

o2 = Parent2()
print(o2.mul(4, 6))
print(o2.mul(7))
print(o2.mul(2, 5, 8))
