#if and else statement
age = int(input("enter your age: "))
print("your age is ", age)

if(age >= 18):
    print("you can vote")
else:
    print("you can't vote\n")

#elif statement
num = int(input("enter your num: "))
print("your num is ", num)
if(num == 0):
    print("number is neutral")
elif(num > 0):
    print("num is positive")
else:
    print("num is negative")

#nested statement
budget = int(input("enter your amount: "))
print("your budget is: ", budget)
if(budget < 50):
    if(budget < 40):
        print("bring pasta with masala")
    elif(budget < 20 ):
        print("bring maggi")

elif(budget < 100):
    print("go black square")

else:
    print("water")
