#class ParentClass:
#    def parent_method(self):
#        print("this is a parent method.")
#
#class ChildClass(ParentClass):
#    def parent_method(self):
#        print("abhijeet")
#    def child_method(self):
#        print("this is a child method.")
#        super().parent_method()
#
#child_object = ChildClass()
#child_object.child_method()

class Employee:
    def __init__(self, name , id):
        self.name = name 
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.name = name
        super().__init__(name,id)
        self.lang = lang

rohan = Employee("rohan das", "420")
harry = Programmer("harry","2345","python")
print(rohan.name)