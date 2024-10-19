#dir()

#x = [1,2,3]
#print(dir(x))

#from output we get methods can be run
#print(x.count)


#__dict__
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

P = Person("abhijeet", 20)
print(P.__dict__)               #gives dictionary

print(help(Person))             #used to give description of code
