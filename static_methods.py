class math:
    def __init__(self, num):
        self.num = num

    def addtwonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a + b
    
#result = math.add(1,2)
    
a = math(5)
print(a.num)
a.addtwonum(6)
print(a.num)

