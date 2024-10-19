#while loop (incremental loop)
i = 0
while(i < 5):
    print(i)
    i = i + 1
print("chal gya bhai loop")


#while with input (incremental loop)
a = int(input("enter the number:  "))
while(a < 100):
    print(a)
    a = a + 1
print("chal gya bhai loop")


#while with else statement (decremental loop)
count = 5 
while(count > 0):
    print(count)
    count = count - 1
else:
    print("I'm inside else")


#do-while loop
j = 1 
while True: 
	print(j) 
	j = j + 1 
	if(j > 10): 
		break