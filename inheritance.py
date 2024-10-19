class Employee:
    def __init__ (self,name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee is : {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("the default language is python")


e1 = Employee("abhijeet", 19)
e1.showDetails()
e2 = Programmer("chamdu", 29)
e2.showDetails()
e2.showLanguage()
