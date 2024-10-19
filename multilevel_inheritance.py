class Base:
	def __init__(self, name, id, role):
		self.name = name
		self.id = id
		self.role = role

class Intermediate(Base):
	def __init__(self, age, name, id, role):
		super().__init__(name, id, role)
		self.age = age

class Derived(Intermediate):
	def __init__(self, age, name, id, role):
		super().__init__(age, name, id, role)

	def show(self):
		print(f"The Name is : {self.name}")
		print(f"The Age is : {self.age}")
		print(f"The role is : {self.role}")
		print(f"The id is : {self.id}")

obj = Derived(21, "Lokesh Singh", 25, "Software Trainer")
obj.show()
