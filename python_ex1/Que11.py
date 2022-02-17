# Create another script/program using 'input' and pass all the three parameters as a
# single input and execute the same program as mentioned above.

(a, b, c) = map(int, input().split())
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
