import threading
import time

#indicates some task being alone 
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
#func(4)
#func(2)
#func(1)


#same code using thread
t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[2])
t3 = threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

#calculating time
time2 = time.perf_counter()
print(time2-time1)