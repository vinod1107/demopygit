from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

# below allows t1 & t2 to complete and then allows the main thread print "Bye"
t1.join()
t2.join()
print("Bye")
