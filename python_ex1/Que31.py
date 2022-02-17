class My_parent_class:
    x = 2
    y = 1

    def __init__(self, a=0, b=0):
        if not a and not b:
            pass
        else:
            self.x, self.y = a, b

    def add(self):
        res1 = self.x + self.y
        return res1

    def sub(self):
        res2 = self.x - self.y
        return res2

    def print_result(self):
        print("Addition :", self.add(), "\t","Subtraction: ", self.sub())

    def __del__(self):
        print("Destructor called")


class My_child_class(My_parent_class):
    z = 4

    def __init__(self, c=0):
        super().__init__()
        if not c:
            pass
        else:
            self.z = c

    def add(self):
        return super(My_child_class, self).add() + self.z

    def sub(self):
        return self.x * self.y * self.z

    def print_result(self):
        print("Addition :", self.add(), "\t","Subtraction: ", self.sub())

    def __del__(self):
        print("Destructor Called")


o1, o2, o3 = My_parent_class(), My_parent_class(6), My_parent_class(8, 4)
c1, c2 = My_child_class(), My_child_class(3)
o1.print_result(), o2.print_result(), o3.print_result()
c1.print_result(), c2.print_result()
del o3
