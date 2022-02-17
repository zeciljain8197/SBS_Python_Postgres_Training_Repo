def validate():
    a = 19.23
    b = 20
    if type(a) is float and type(b) is int:
        print(a + b)
        return True


print(validate())
