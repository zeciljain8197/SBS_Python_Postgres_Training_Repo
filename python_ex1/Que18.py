# Create a function that will take unlimited arguments and should add all the
# arguments which are passed.

def sum(*args):
    Sum = 0
    lst1 = []
    for arg in args:
        lst1.append(arg)
        Sum += arg
    print("Result: ", Sum)


lst = list(map(int, input("Please enter the arguments to be taken: ").split()))
sum(*tuple(lst))
