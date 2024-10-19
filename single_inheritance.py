class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal")


class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name , breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("meow")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog","Dog")
a.make_sound()

b = Cat("Cat","russian")
b.make_sound()