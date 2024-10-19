class employee:
    def __init__(self):                 
        #self.name = "abhijeet"              #public
        self.__name = "abhijeet"             #private

    def _funname(self):                      #protected
        return("code with harry")
    
class Subject(employee):                     #inherited class
    pass

a = employee()

#access public specifier         
#print(a.name)

#access private specifier

#print(a._employee__name)                #cant be accessed directly      #name mangling
#print(a.__dir__())         


#access protected specifier
b = Subject()
print(dir(a))

print(a._name)                          #calling object from employee class
print(a._funname)

print(b._name)                          #calling object from subject class
print(b._funname)