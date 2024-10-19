marks = [4,5,6,"abhijeet", True, 7, 0 , 12, "red"]                          #list is in square brackets
                                                    #list changes tuples not
print(marks)

print(type(marks))

print(marks[0])                          #accessing list using index
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
 
print(marks[-3])                         #accessing list by negative indexing
print(marks[len(marks)-3])               #negative to positive indexing
print(marks[5-3])                       


#to find some value
if "abhijeet" in marks:
    print("yes its there")
else:
    print("no its not there")


#to find string under string
if "jeet" in "abhijeet":
    print("yes its there")
else:
    print("no its not there")


#accessing list using range
print(marks)
print(marks[ :5])
print(marks[1 : -1])
print(marks[1 : 4 : 2])                         #jump index


#list comprehension

list = [i for i in range(4)]
print(list)

another_list = [i*i for i in range(20) if i%2==0]        
print(another_list)


