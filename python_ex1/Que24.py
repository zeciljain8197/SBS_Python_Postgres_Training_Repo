# Create a function that will take 5 arguments 2 will be mandatory and 3 will be
# keyword parameters. If 2 parameters are passed perform multiplication of 2
# parameters. If 3 parameters are passed print all the 3 parameters. If 4 parameters
# are passed addition of 4 parameters. If 5 parameters are passed multiply 2
# mandatory parameters and then separately multiply 3 keyword parameters and add
# both of them.

def func(a, b, c=0, d=0, e=0):
    if not c and not d and not e:
        return a * b
    elif not d and not e:
        return a, b, c
    elif not e:
        return a + b + c + d
    else:
        return (a * b) + (c * d * e)


print("Enter the number of inputs to be taken: ")
n = int(input())
if n == 2:
    i, j = map(int, input("Enter the inputs: ").split())
    o1 = func(i, j)
    print(o1)
elif n == 3:
    i, j, k = map(int, input("Enter the inputs: ").split())
    o2 = func(i, j, k)
    print(o2)
elif n == 4:
    i, j, k, m = map(int, input("Enter the inputs: ").split())
    o3 = func(i, j, k, m)
    print(o3)
else:
    i, j, k, m, o = map(int, input("Enter the inputs: ").split())
    o4 = func(i, j, k, m, o)
    print(o4)
