import time

def usingWhile():
    i = 0
    while i < 5000:
        i = i + 1
        print(i)
    pass

def usingFor():
    for i in range(50000):
        print(i)
    pass

#time taken by for loop to write all counting
init = time.time()
usingFor()
t1 = time.time() - init

#to make the code wait 
time.sleep(2)

#time taken by while loop to write all counting
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

time.sleep(2)

#local time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)