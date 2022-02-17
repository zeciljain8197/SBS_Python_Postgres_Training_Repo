a = 10
b = "9.8"
try:
    sum = float(a + b)
    print(sum)
except Exception as e:
    print(e)
else:
    print("try part executed successfully!!")