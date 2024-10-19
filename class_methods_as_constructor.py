class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
e = Employee("abhijeet", 100000)
print(e.name)
print(e.salary)

string = "Abhijeet-120000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
    
person = person.from_string("john cena, 30")
print(person.name, person.age)