# Implement multiple inheritance and multi-level inheritance.

class Father:
    a = 5
    b = 9

    def sum(self):
        return self.a + self.b


class Mother:
    a = 10
    b = 3

    def sum(self):
        return self.a + self.b


class Child1(Father, Mother):
    def sum(self):
        return self.a - self.b


class Child2(Mother, Father):
    def sum(self):
        return self.a - self.b


class Grandchild1(Child1):
    def sum(self):
        return self.a + self.b


class Grandchild2(Child2):
    def sum(self):
        return self.a + self.b


o1 = Father()
o2 = Mother()
o3 = Child1()
o4 = Child2()
o5 = Grandchild1()
o6 = Grandchild2()
print("Father Result: ", o1.sum(), "\n","Mother Result: ", o2.sum(), "\n","Child1 Result: ", o3.sum(), "\n","Child2 Result: ", o4.sum(), "\n","Grandchild1 Result: ", o5.sum(), "\n","Grandchild2 Result: ", o6.sum())