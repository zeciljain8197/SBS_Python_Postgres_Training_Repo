def test_dec_func(a, b):
    def def_func(func):
        def var():
            n = a * b
            return func(n, b)

        return var

    return def_func


@test_dec_func(6, 7)
def test_func(n, b):
    print(n * b)


test_func()
