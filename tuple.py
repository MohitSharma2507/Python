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


#   Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)