#used for string formating

a = "my name is {} and I am from {}"
country = "India"
name = "abhijeet"
print(a.format(name, country))



#fstring
name1 = "Abhijeet thakur"
b = f"my name is {name1} and I am from {country}"
print(b.format(name1, country))


#playing with float values
Price= 49.998898
price = f"for only {Price: .2f} dollars!"
print(price)


print(type(f"{2*30}"))                              #datatype