# Print odd numbers between 1 and 10 in reverse order using while.

n = 10
while n > 0:
    if n % 2 != 0:
        print(n)
        n -= 1
    else:
        n -= 1
    