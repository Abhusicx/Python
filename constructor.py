class person:
    #name = "abhijeet"
    #occ = "developer"
    def __init__(self, name , occ):
        print("hey i'm ")
        self.name = name
        self.occ = occ
        
    def info(self):
        print(f"{self.name} and i'm an {self.occ}")
        
a = person("harry", "developer")
b = person("divya", "HR")
#c = person(1,2,3)
a.info()
b.info()
#print(a.name)
#a.name = "divya"
#a.occ = "HR"
#a.info()