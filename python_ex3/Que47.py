def pg(num):
    for n in range(2, num):
        for a in range(2, n):
            if n % a == 0:
                break
        else:
            yield n


res = pg(100)
print(list(res))

