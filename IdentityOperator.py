a=5
b=6
c=5

print(a is c)
print(a == b)
print(id(a))  # to check the memory address/id of the variable
print(id(b))
print("checking with string")
d=6
e='6'

print(d is not e)
print(d == int(e))
print(type(d))
print(type(e))
print(id(d))
print(id(e))

print("checking with float")
d=6
e=6.0

print(d is e)
d=8
print(id(d))
print(d is d)
print(d is not e)
print(d == int(e))
print(d == e)
print(type(d))
print(type(e))
print(id(d))
print(id(e))
