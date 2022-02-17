import cProfile
import time
import pstats

pr = cProfile.Profile()
pr.enable()
f = open('Creds.py', 'r')
res1 = f.readline()
res2 = f.readline()
print(res1)
time.sleep(2)
print(res2)
pr.disable()
p = pstats.Stats(pr)
p.print_stats()
