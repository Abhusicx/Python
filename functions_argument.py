def average(a = 1,b = 2):
    print("average is: ", (a+b)/2)

average(5,6)                            #higher priority

average(b=0)                            #higher priority




def fullname(fname, mname = "singh", lname = "yadav"):              #string
    print("hello", fname, mname, lname)
    print(type(fullname))

fullname("uday")