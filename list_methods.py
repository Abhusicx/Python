#manipulating list with its methods
l = [1,2,6,2,3,4]
print(l)

l.append(5)                             #insert item in list
print(l)

l.sort                                  #sorting
print(l)


l.sort(reverse=True)                    #descensding sorting
print(l)


l.reverse                               #reverse list
print(l)


print(l.index(2))                       #index of item in list

print(l.count(2))                       #count item in list


m = l                                   #inserting by merging another list on whatever index you want
m[0] = 10
print(l)


m = l.copy                              #recommended
m[10]=29
print(l)


l.insert(1, 899)                        #inserting 899 at index[1]
print(l)


n = [900, 1000, 1100,1200]              #extending original  list
l.extend(m)
#k = l+m
#print(k)
print(l)



