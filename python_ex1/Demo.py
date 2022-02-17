class My_parent_class:
    res1 = 0
    res2 = 0

    def __init__(self, a, b, c=0, d=0):
        self.w, self.x = a, b
        while c is int:
            self.y = c
        while d is int:
            self.z = d

    def add(self, a, b, c=0, d=0):
        return a + b + c + d

    def sub(self, a, b, c=0):
        return a - b - c

    def calc(self):
        if not self.y and not self.z:
            self.res1 = self.add(self.w, self.x)
            self.res2 = self.sub(self.w, self.x)

        elif not self.z:
            self.res1 = self.add(self.w, self.x, self.y)
            self.res2 = self.sub(self.w, self.x, self.y)

        else:
            self.res1 = self.add(self.w, self.x, self.y, self.z)
            self.res2 = self.sub(self.w, self.x, self.y)

    def print_result(self):
        print("Addition result: ", self.res1, "\t", "Subtraction result: ", self.res2)


p1 = My_parent_class(4, 8, 6, 5)
p2 = My_parent_class(4, 8, 3)
p3 = My_parent_class(4, 8)
p1.calc()
p2.calc()
p3.calc()
p1.print_result()
p2.print_result()
p3.print_result()
