class Parent:
    x = 73
    y = -3
    z = 49

    def add(self):
        return self.x + self.y + self.z

    def mul(self):
        return self.x * self.y * self.z

    def sub(self):
        return self.x - self.y - self.z


def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1
