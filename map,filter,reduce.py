#def cube(x):
#   return x*x*x
#
#print(cube(2))

#map
#l = [1,2,4,6,4,3]
#newl = []
#for item in l:
#    newl.append(cube(item))

#newl = list(map(cube,l))
#print(newl)


#filter
#a = [1,2,4,6,4,3]
#def filter_function(a):
#    return a > 4

#newa = list(filter(filter_function, a))
#print(newa)


#reduce

from functools import reduce 

num = [1,2,3,4,5]

#calculate sum

sum = lambda x, y: x+y
sum = reduce(sum,num)

print(sum)