import threading
import time


def func1():
    print("Function 1 started..")
    time.sleep(2)
    print("Function 1 Ended")


def func2():
    print("Function 2 started..")
    time.sleep(3)
    print("Function 2 Ended")


def func3():
    print("Function 3 started..")
    time.sleep(1)
    print("Function 3 Ended")


start = time.time()

thread1 = threading.Thread(target=func1, args=())
thread2 = threading.Thread(target=func2, args=())
thread3 = threading.Thread(target=func3, args=())

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

end = time.time()
print("Main Ended in .. ", end - start)

