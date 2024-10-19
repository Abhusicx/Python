countries = ("india", "australia", "japan", "USA", "UK", "india")
print(countries)

temp = list(countries)                              #tuples can be changed but not directly


temp.append("russia")                               #add item
#temp.pop("australia")                               #remove item      
temp[2] = "newzealand"                              #replace item

countries = tuple(temp)                             #converting temp back to tuple
print(countries)


res = countries.count("india")                      #count in tuple
print(res)


#res1 = countries.index(3)                           #find  using index
#print(res1)


#change tuple to list then do changes in list and then convert it again to tuple


