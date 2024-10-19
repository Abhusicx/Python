class Employee:
    company = "apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "abhijeet"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)