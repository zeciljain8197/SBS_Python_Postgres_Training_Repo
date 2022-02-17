# Create a constructor and destructor for the above class.

class Parent:
    def __init__(self):
        print("Constructor initialised")

    def sum(self, count):
        count += 1
        return count

    def mul(self, count):
        count *= 5
        return count

    def __del__(self):
        print("Destructor initialised")


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

