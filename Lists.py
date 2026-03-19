# List are mutable means once you create a list you can modify/change it

# marks = ["Mohit",23,"98"]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# #List Methods

list = [1,2,3,6,4,5,6]

# list.append(7) #Adds one more elements at the end
# list.sort() #Sorts in ascending order
# list.sort(reverse=True) #Sorts in descending order
# list.reverse() #Reverse list
# list.insert(1,"Rohit") #insert elment at index
# list.remove(1) #removes first occurance of element
# del list[1] #deltes the selected index
# list.clear() #empty the list
list.extend([45,46,47,48])#Add the numbers in the last of the list
print(list[1:4] )#Slicing [index where to start(include):Length where to end(include)]
print(list[1:4:2] )#Slicing [index where to start(include):Length where to end(include):steps to skip]
list[1:5]=[50,51,51]
print(list)
# list.pop(6) #removes first occurance of element
# print(list)


# movies = []
# movies.append(input("Enter the 1st movie : "))
# movies.append(input("Enter the 2nd movie : "))
# movies.append(input("Enter the 3rd movie : "))

# print(movies)

# list1 = [1, 2, 3, 2, 1]
# is_palindrome = True  # flag

# for i in range(len(list1)):
#     if list1[i] != list1[len(list1)-1-i]:
#         is_palindrome = False
#         break  # no need to check further

# if is_palindrome:
#     print("List is palindrome")
# else:
#     print("List is not palindrome")
               

# list1 =[1,2,3,2,1]
# list2 = list1.copy()
# list2.reverse()
# flag = True

# if(list1==list2):
#     print("List is palidrome")
# else :
#     print("List is not palidrome")
