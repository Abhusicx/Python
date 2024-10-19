class Employee:
    #name = "abhijeet"
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i 
    def __str__(self):
        return f"the name of the employee is {self.name}"
    
    def __repr__(self):
        return f"the name of the employee is {self.name} repr"


e = Employee()
print(e.name)
print(len(e))


#make a new file and copy the code

#from emp import Employee
#e = Employee("harry")
#print(e)