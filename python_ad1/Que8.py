import cProfile
import time
import pstats
import mymodule

pr = cProfile.Profile()
pr.enable()


def var(a, b):
    res1 = mymodule.add(a, b)
    time.sleep(1)
    res2 = mymodule.sub(a, b)
    time.sleep(2)
    res3 = mymodule.mul(a, b)
    time.sleep(2)
    res4 = mymodule.div(a, b)
    time.sleep(1)
    print(res1, res2, res3, res4)


var(18, 3)
pr.disable()
p = pstats.Stats(pr)
p.print_stats()
