import random
import threading
import time


class MyT(threading.Thread):
    def __init__(self, a, b, threadID, name, counter, delay):
        super(MyT, self).__init__()
        self.a = a
        self.b = b
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print(random.randrange(self.a, self.b))
        print_time(self.name, self.counter, self.delay)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = MyT(1, 10, 1, "Thread1", 3, 3)
thread2 = MyT(11, 20, 2, "Thread2", 4, 2)
thread3 = MyT(21, 30, 3, "Thread3", 1, 3)

thread1.start()
thread2.start()
thread3.start()

print("Exiting main thread")
