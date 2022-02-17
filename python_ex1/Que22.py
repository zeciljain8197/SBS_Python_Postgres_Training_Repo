# Create a script/program that will take arguments as 1,2,3,4,5, or 6 and will also
# take operands as arguments based on the selection made it will perform the
# operation and print the result.
# • 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Exponent,
# 6=Floor Division. If anything else is passed it should say Invalid argument.
# • Create a parent function which will accept the options and based on the options
# it will call nested functions for each operation. So total 7 functions will be
# created one parent and 6 nested functions.
# • According to the selection made take inputs for the operations. If 1,2,3 are
# selected take 3 inputs as operands and if 4,5,6 are selected take 2 inputs as
# operands. Perform the operation and print the result.

def selection(a):
    if 1 <= a <= 3:
        i, j, k = map(int, input().split())

        def ad(i, j, k):
            return i + j + k

        def sb(i, j, k):
            return i - j - k

        def ml(i, j, k):
            return i * j * k

        if a == 1:
            return ad(i, j, k)
        if a == 2:
            return sb(i, j, k)
        if a == 3:
            return ml(i, j, k)
    else:
        i, j = map(int, input().split())

        def dv(i, j):
            return i / j

        def ep(i, j):
            return i ** j

        def fd(i, j):
            return i // j

        if a == 4:
            return dv(i, j)
        if a == 5:
            return ep(i, j)
        if a == 6:
            return fd(i, j)


z = int(input("Enter the choice: "))
print(selection(z))
