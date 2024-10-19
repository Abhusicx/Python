#functions perform specific task whenever called

def calculate_geometric_mean(a,b):              #function (user defined done by def keyword)
    mean = (a*b)/(a+b)
    print(mean)

def isgreater(a,b):                             #function (user defined done by def keyword)
    if(a > b):
        print("a is greater")
    elif(b < a):
        print("b is greater")
    else:
        print("they are equal")

def islesser(a,b):
    pass                                        #pass means currently not available baad me likhunga but error ni aayega


#use of function
a = b = 9
calculate_geometric_mean(a,b)                   #function call
isgreater(a,b)

c = d = 10
calculate_geometric_mean(c,d)                   
isgreater(c,d)                                  #function call