from threading import Thread
import time

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello") 
            time.sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            time.sleep(1)

t1 = hello()
t2 = hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("fsfdsfsfs")
