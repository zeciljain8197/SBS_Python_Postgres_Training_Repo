# Write a function with recursion to give the power of a number. It will be having
# two parameters no. and power. If no power is passed it should take 0.

def power(number, pwr):
    pr = int(pwr)
    if pr > 1:
        return number * power(number, pr-1)
    else:
        return 1


a = int(input("Enter the number: "))
b = input("Enter the power to be calculated: ")
if len(b) == 0:
    print("Result: ", power(a, 0))
else:
    print("Result: ", power(a, b))



