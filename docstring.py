#its like comment but doesn't get ignored like comment

def square(n):
    #print(n)                               #this will make docstring none
    '''takes a number n, returns the square of it'''

    print(n**2)                             #square

square(5)
print(square.__doc__)                       #to see docstring
