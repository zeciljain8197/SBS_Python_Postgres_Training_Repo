# Create a function which will take 4 arguments where 2 wil be mandatory and 2
# keyword arguments. Perform multiplication if 2 values are passed. Perform
# addition if 3 are passed. Perform addition of 1st two operands and 2nd two operands
# and then do a subtraction if 4 arguments are passed.

def func1(*args):
    lst1 = []
    for arg in args:
        lst1.append(arg)
    if len(lst1) == 2:
        return lst1[0]*lst[1]
    elif len(lst1) == 3:
        return lst1[0] + lst[1] + lst[2]
    else:
        return (lst1[0] + lst[1]) - (lst[2] + lst[3])


lst = []
z = int(input("Enter the no of input: "))
if 2 <= z <= 4:
    for i in range(z):
        lst.append(int(input()))
    print(func1(*tuple(lst)))
else:
    print("Please enter valid number of inputs!")







