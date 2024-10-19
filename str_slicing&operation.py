#length of string
a = "abhijeet"
print(len(a))

#uppercase
b = "abhijeet"
print(b.upper())

#lowercase
c = "ABHIJEET"
print(c.lower())

#strip trailing character
d = "!!abhijeet!!!"
print(d.rstrip)

#replace
e = "abhijeet"
print(e.replace("abhi","baadme"))

#split
f = "Nalla Arbaj"
print(f.split(" "))
print(type(f.split())) #list

#capilalize
g = "kunal"
print(g.capitalize())

#center
h = "kunal"
print(h.center(50))
print(len(h))
print(len(h.center(50)))

#count
i = "abracadabra"
print(i.count("a"))

#endswith
j = "yezz yezz!"
print(j.endswith("!"))

#find
k = "krsna"
print(k.find("r"))
print(k.find("y")) 

#index
l = "dumb"
print(l.index("genius"))

#isalnum
m = "@bhijeet"
print(m.isalnum())

#isalpha
n = "sakshy"
print(n.isalpha())

#islower and isupper
o = "Moron"
print(o.islower())
print(o.isupper())


#isprintable
p = "i will \n do it"
print(p.isprintable())

#istitle
q = "hail Hydra"
print(q.istitle())

#startswith
r = "! rola on top"
print(r.startswith())

#swapcase
s = "Start"
print(s.swapcase())

#title
t = "abhijeet thakur"
print(t.title())

