me = {
    "name" : "abhijeet thakur",
    "age" : 20,
    "salary" : "none"
}

print(me["name"])
print(me["age"])
print(me["salary"])


student = {'name':'uday', 'age':19, 'eligible':True}
print(student)
print(student["name"])
print(student.get('name1'))                 #through error if key not present

print(student.keys())                       #to know keys

#alternative way
for key in student.keys():
    print (f"the value corresponding to the key {key} is {student[key]}")


#to get items
print(student.items())
for key, value in student.items():
    print(f"the value corresponding to key{key} is {value}")


