# Create a python script/program that will take input from the user for 3 numbers
# and result will print the biggest number and the smallest number using 'input' and
# 'print'.

a = int(input())
b = int(input())
c = int(input())
if a > b:
    if b > c:
        print("Greatest number is =", a, "\n", "Smallest number is =", c)
    else:
        if a > c:
            print("Greatest number is =", a, "\n", "Smallest number is =", b)
        else:
            print("Greatest number is =", c, "\n", "Smallest number is =", b)
else:
    if a > c:
        print("Greatest number is =", b, "\n", "Smallest number is =", c)
    else:
        if b > c:
            print("Greatest number is =", b, "\n", "Smallest number is =", a)
        else:
            print("Greatest number is =", c, "\n", "Smallest number is =", a)
