d = 12


def test_func():
    global x
    x = 20
    y = 9

    print("Locals in func", locals())
    print("Globals in func", globals())

    def nest_func():
        y = 30
        global a
        a = "Zecil_Jain"
        print("Locals in nest func", locals())
        print("Globals in nest func", globals())

    nest_func()


test_func()
print("Locals of main func:", locals())
print("Globals of main func:", globals())
