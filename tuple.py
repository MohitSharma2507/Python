# Tuples are immutable means once you create a tuple you can't modify/change it

tup1 = (1,2,3,4,2,1)
tup2 = ("Jai",1,2,1.5,"a")

print(tup1.index(4)) #returns index of occurences
print(tup2.count(2)) #counts total 
print(tup2)
print(tup2[3])
tup3=(10,)
tup4=(10)

print(type(tup2))
print(type(tup4))
print(tup2[1:6:2])


tup5 =(tup1,tup2)
print(len(tup5))

tup6 =(tup1 + tup2)
print(len(tup6))

print(tup5)
print(tup6)
print(min(tup1))


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")