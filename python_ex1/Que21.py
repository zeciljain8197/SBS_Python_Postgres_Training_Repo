# Create a function with recursion which will find the factorial of a given no.

def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1


z = int(input("Enter the number: "))
print(fact(z))
