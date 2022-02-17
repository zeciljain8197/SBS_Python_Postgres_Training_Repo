# Create a parent class and a child class. Create two methods in the parent class.
# Create one method in the child class. Create an object of parent and try to access
# the method of parent and child class. Create an object of child class and try to
# access the method of parent and child class.

class Parent:
    def sum(self, count):
        count += 1
        return count

    def mul(self, count):
        count *= 5
        return count


class Child(Parent):
    def sub(self, count):
        count -= 1
        return count


o1 = Parent()
o2 = Child()
print(o1.sum(5))
print(o1.mul(5))
# print(o1.sub) - Parent class can't access child class methods or variables
print(o2.sum(5))
print(o2.mul(5))
print(o2.sub(5))

