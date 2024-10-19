class MyClass:
    def __init__(self,value):
        self._value = value

    def show(self):
        print(f"value is {self._value}")

    @property                   #getter
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter           #setter
    def ten_value(self, new_value):
        self._value = new_value/10
    
obj = MyClass(10)
obj.ten_value = 69
obj.Ten_value = 69
print(obj.ten_value)
print(obj.Ten_value)
obj.show()