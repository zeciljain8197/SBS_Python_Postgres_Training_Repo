class Test:
    a = 10
    b = 20
    c = 30


res1 = hasattr(Test, 'b')
print(res1)
res2 = getattr(Test, 'a')
print(res2)
res3 = setattr(Test, 'c', 45)
res4 = getattr(Test, 'c')
print(res4)
res5 = delattr(Test, 'c')
res6 = getattr(Test, 'c')
print(res6)