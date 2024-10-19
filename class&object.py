class person:
    name = "abhijeet"
    occupation = "software engineer"
    networth = "10000$"

    def info(self):                     #self is parameter of current instance of class
        print(f"{self.name} is a {self.occupation} with {self.networth}")


#object
a = person()
b = person()
#a.name = "parth"
#a.occupation = "head master"
#a.networth = "1000000$"

b.name = "nitika"
b.occupation = "HR"
print(a.name, a.occupation, a.networth)
a.info()
b.info()