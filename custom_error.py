salary = int(input("enter salary amount: "))

if(salary <= 20000):
    print("valid salary")
else:
    raise ValueError("not a valid salary")


