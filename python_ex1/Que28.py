# Override and Overwrite a method of the parent class in child class.

class Parent:
    a = 5
    b = 8

    def sum(self):
        return self.a + self.b


class Child(Parent):
    def sum(self):
        return self.a - self.b


o1 = Parent()
o2 = Child()
print("Parent Method result: ", o1.sum())
print("Child Method result: ", o2.sum())
