class Employee:
    companyName = "apple"               #class variable
    numofemployee = 0
    def __init__(self, name):
        self.name = name                #instance variable
        self.raise_amount = 0.02
        #self.noofemployee +=1
    def showDetails(self):
        print(f"the name of employee is {self.name} and the raise amount is {self.raise_amount} and the company is {self.companyName} and no. of employee are: ")

emp1 = Employee("harry")
emp1.companyName = "microsoft"              #instance variable
emp1.showDetails()
#Employee.showDetails(emp1)


emp2 = Employee("abhijeet")                 #by default will use class variable
emp2.raise_amount = 0.07
emp2.showDetails()