"""
try:
    statement which could generate
    exception
except:
    solution of generated exception
finally:
    block of code which is going to execute in any situation
"""


#a = input("enter the no. ")                         #what is someone input there name instead of number ?? 
#print(f"multiplication table of {a} is: ")
#agar error aaye toh kuch or hojaye
#try:
#  for i in range (1, 11):
#    print(f"{int(a)} X {i} = {int(a)*i}")
#except : 
#  print("invalid input")
#
#print("some imp lines of code")
#print("end of program")

try:
    num = int(input("enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("value entered is not an integer")

except IndexError:
    print("Index Error")