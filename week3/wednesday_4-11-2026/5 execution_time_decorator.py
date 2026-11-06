import time

def main(func):
    def wapper():
        start = time.time()
        print("start")
        func()
        print("stop")
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wapper


@main
def time1():
    for i in range(1000000):
        pass


time1()