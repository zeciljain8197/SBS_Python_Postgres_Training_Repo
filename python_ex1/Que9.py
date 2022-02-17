# Perform operations with all the Logical Operators

a = int(input())
b = int(input())
c = int(input())

if a >= 0 and b >= 0:
    print("Both numbers are positive")
if not c >= 0:
    print("C is negative")
if b > c > a or a > c > b:
    print("C lies between A and B")
