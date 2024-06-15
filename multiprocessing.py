import multiprocessing as mp
import time
import math


result_a = []
result_b = []
result_c = []

def sq1(numbers):
    for i in range(numbers):
        result_a.append(math.sqrt(i ** 2))
    
def sq2(numbers):
    for i in range(numbers):
        result_b.append(math.sqrt(i ** 3))

def sqr3(numbers):
    for i in range(numbers):
        result_c.append(math.sqrt(i ** 4))

if __name__ == '__main__':
    numbers = 10000000
    print("hi")

    mp1 = mp.Process(target=sq1,args=(numbers,))
    mp2 = mp.Process(target=sq2,args=(numbers,))
    mp3 = mp.Process(target=sqr3,args=(numbers,))

    start = time.time()
    mp1.start()
    mp2.start()
    mp3.start()
    end = time.time()
    print(end - start)

    start = time.time()
    sq1(numbers)
    sq2(numbers)
    sqr3(numbers)
    end = time.time()
    print(end - start)
