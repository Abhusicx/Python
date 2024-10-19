#for loop
name = "abhijeet"
for i in name:
    print(i, end=",")


#for loop with if statement
name = "chamdu"
for i in name:
    print(i,end=",")
    if(i == "u"):
        print("pervert")


#for loop inside a for loop
color = ("green goblin", "light yagami",)
for color in color:
    print(color)
    for i in color:
        print(i)


#for loop for number inside range
for i in range(6):
    print(i)            #prints 0 to 5
    print(i+1)          #prints 0 t0 6


#for loop for range of number inside range
for i in range(1,10):
    print(i)            #prints 1 to 9


#for loop range(start,stop,step)
for i in range(0, 15, 3):
    print(i)
