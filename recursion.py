#function inside function

def factorial (n):
    if (n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return n * factorial(n-1)                   #same function inside same function is recursion
    
print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(4))
print(factorial(5))