a = []
i = int(input("Enter the number of inputs to be taken: "))
for _ in range(i):
    if i < 5:
        raise Exception("Minimum length of list should be 5")
    n = int(input("Enter the number: "))
    a.append(n)
print(a)

