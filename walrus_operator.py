a = True
#to make it false
print(a:=False)                 #walrus operator


num = [1,2,3,4,5]

while(n:=len(num))>0:
    print(num.pop())



happy = True
print(happy)
print(happy:=True)



foods = list()
#while True:
#    food = input("what food you want?")
#    if food == "quit":
#        break
#    foods.append(food)

#alternative of above code using walrus 
while(food:= input("what food you like?: ")) != "quit":
    foods.append(food)