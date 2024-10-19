#match case
x = int(input("enter your value: "))
match x:
    case 0:
        print("x is neutral")
    case 1:
        print("x is positive")
    case -1:
        print("x is negative")
    case _ if x > 10:    #condition in match case
        print("x is big number")
    case _:
        print(x) #default