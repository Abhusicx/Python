#break statement
for i in range(12):
    if(i==10):
        
        break
    print("5 x ", i+1, "=", 5 * (i+1))

print("loop ko chodkar nikal liya")


#continue statement
for j in range(12):
    if(j==10):
        print("iteration skipped")
        continue
    print("5 x ", j+1, "=", 5 * (j+1))

print("loop ko chodkar nikal liya")


#do-while using break and continue
k = 0
while True:
    print(k)
    k = k + 1
    if(k == 100):
        break