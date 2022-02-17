# Define a class and define two member variables and two methods inside the class.
# One method will have one parameter and other method will not have any
# parameter. Create a constructor for the class accepting two parameters and assign
# them to the class member variables. One of the two methods will perform an
# operation on the member variables and give result. The second method will print
# the result.

class Parent:
    a = 4
    b = 7

    def __init__(self, x=0, y=0):
        x = self.a
        y = self.b

    def add(self, a):
        self.a += self.b
        return self.a

    def print_result(self):
        print(self.add(self.a))


o1 = Parent()
o1.print_result()
