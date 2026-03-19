import random

# s1 = "MySirji"

# for a in s1 :
#     print(a , ord(a)) 

# First 10 Odd natural number


# 1. for i in range(1, 20, 2):  # start=1, stop=20, step=2
#     print(i, end = " ")


# 2. count = 0
#    num = 1

# while count < 10:
#     print(num)
#     num += 2
#     count += 1
 

# Write a python script to calculate factorial of a number

# num = int(input("Enter a number: "))
# factorial = 1

# if num < 0:
#     print("Factorial does not exist for negative numbers.")
# elif num == 0:
#     print("The factorial of 0 is 1.")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")

#! LOOPs 

# for key, value in enumerate("Python"):
#     print(key,value)
# !
# for value in ["Mohit","Ankit","Jai"]:
#     print(value)
# !
# for value in range(1,10 ,2):
#     print(value)
# !
# for i in range(4):
#     for j in range(4):
#         print(f"({i},{j})")   
# !
# for i in [2,2,2,2,6]:
#     for j in range(i):
#       print(i*"X")
#       break
    
#! LIST 

# names1 = input("Enter the heights by comma separated : ").split(",")
# sum=0
# count=0
# for i in names1:
#     sum+=int(i)
#     count+=1

# print(round(sum/count))   


# Find Max number in list

list1= [1,2,3,4,51,6,117,811,19,10]
count=0
max=0

for i in list1:
   count+=1

for i in range(count):
    if list1[i]>max:
        max=list1[i]

print(f"Maximum number in list is {max}")




