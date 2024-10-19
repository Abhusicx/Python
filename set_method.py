a = {1,2,3,5}
b = {2,4,6,7}

#joining two set
print(a.union(b))                   

#not updated
print(a,b)                          

#updated a
a.update(b) 

#updated b
b.update(a)                         
print(a,b)

#intersection
c = a.intersection(b)         

#intersection update
c = a.intersection_update(b)        
print(c)                

#symmetric difference       #non common values
d = {4,5,9,2,65,1}
print(c.symmetric_difference(d))

#symmetric difference update
e = c.symmetric_difference_update(d)
print(e) 

#remove item
d.remove(65)

#add item
d.add(99)
d.update()
print(d)


#difference
cities = {"tokyo","madrid", "berlin", "delhi"}
cities2 = {"tokyo", "seoul", "kabul", "madrid"}
cities3 = cities.difference(cities2)                #cities - cities2
print(cities3)


#difference_update
cities3 = cities.difference_update(cities2)
print(cities3)


##isdisjoint
print(cities.isdisjoint(cities2))


#issuperset
print(cities.issuperset(cities3))


#issubset
print(cities.issubset(cities2))


#discard
print(cities.discard("tokyo"))


#pop
print(cities.pop())
print(cities)


#delete set
del cities


#clear
print(cities2.clear())


#to find value in set
info = {"carla", 18 , True}
if "carla" in info:
    print("yus present")
else: 
    print("absent")