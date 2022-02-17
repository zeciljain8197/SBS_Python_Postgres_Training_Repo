g_var = 12
class A:
    def method1(self):
        l_var = 0

    def method2(self):
        pass

    def method3(self, a=0):
        print(locals())
        print(globals())


o1 = A()
o1.method3()
