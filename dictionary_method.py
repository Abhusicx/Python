ep1 = {122:45, 123:56, 124:89, 567:98}
ep2 = {222:56, 566:90}

#update dictionary ep1 by ep2
ep1.update(ep2)
print(ep1)

#clear dictionary
ep1.clear()
print(ep1)

#delete item
ep1.pop(122)
print(ep1)

#delete specific item in dictionary
ep1.popitem()
del ep1[122]
print(ep1)


