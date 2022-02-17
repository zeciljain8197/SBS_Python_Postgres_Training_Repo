# Print odd numbers between 1 and 10 using continue in both for and while loop.

n = 10
print("Select the loop to run", "\n", "1:For", "\n", "2:While")
z = int(input())
# 1 While loop
if z == 1:
    while n > 0:
        if n % 2 == 0:
            n -= 1
            continue
        print(n)
        n -= 1

# 2 For loop
elif z == 2:
    for i in range(10):
        if n % 2 == 0:
            n -= 1
            continue
        print(n)
        n -= 1

else:
    print("Please enter valid input!")
