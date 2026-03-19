# # set is a collection of the unordered items[No index]
# # Each element in the set must be unique & immutable

# collections =set() #empty set syntax
# collections = {1,2,3,4,1 , "one","two"} #count dublicates value as 1
# print(len(collections))

# print(collections)

# #Methods

# collections.add(34) #adds an element
# collections.remove(2) #remoes the elemnt
# collections.discard(2) #remoes/discard the elemnt
# collections.clear() #empties the set
# collections.pop() #removes and return the random value

# set1 ={1,2,3}
# set2 ={3,4,5}
# set3 = set1.union(set2) #combines both set values & returns new
# set3 = set1.intersection(set2) #combines commom values & returns new
# print(set3) 



# marks = {}
# mark1 = int(input("Enter the 1st marks : "))
# mark2 = int(input("Enter the 2nd marks : "))
# mark3 = int(input("Enter the 3rd marks : "))

# marks.update({"phy":mark1})
# marks.update({"chem":mark2})
# marks.update({"math":mark3})


# print(marks)    


# SetOperations [Union]

# set1={'Ram','Shyam','Jenny'}
# set2={'Jenny','Jiya','Aakash'}
# set3={'Jai','Ankit','Mohit'}

# print(set1 | set2) #Union
# print(set1.union(set2,set3))
# print(set1.union(("rohit","kishan")))
# # set1.update(set2)
# set1 |=set2
# print(set1)

# SetOperations [Intersection]

# set1={'Ram','Shyam','Jenny'}
# set2={'Jenny','Jiya','Aakash'}

# print(set1 & set2)
# print(set1.intersection(set2))

# set1.intersection_update(set2)
# print(set1)
# print(set2)

# SetOperations [difference]

# set1={'Ram','Shyam','Jenny'}
# set2={'Jenny','Jiya','Aakash'}

# print(set1.difference(('Mohan','Shiva')))
# print(set1.difference(set2))
# print(set1.difference_update(set2))
# print(set1 - set2)
# print(set1  )

# SetOperations [symmetric]

set1={'Ram','Shyam','Jenny'}
set2={'Jenny','Jiya','Aakash'}
set3={'Ankur','Ram','Pradeep'}

print(set1.symmetric_difference(set2))



