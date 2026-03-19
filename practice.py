import  random
# Class
#! 1
# class Student:


#     def __init__(self,name,marks):
#             self.name = name
#             self.marks = marks

# s1 = Student("Mohit",[90,98,86])
# s2 = Student("Jai",[99,91,98])
# s3 = Student("Ankit",[67,86,99])

# array = [s1,s2,s3]

# for ele in array:
#      print(ele.name,ele.marks)

#! 2
# class Circle:

#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#       return   3.14 * self.radius**2

#     def perimeter(self):
#        return 2* 3.14 * self.radius  



# c1 = Circle(3)
# print(c1.area())

#! 3

# class Employee:

#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showdetails(self):
#             print("role = ",self.role)        
#             print("department = ",self.dept)        
#             print("salary = ",self.salary)        

# class Enginner(Employee):
    
#      def __init__(self,name,age):
#           self.name = name
#           self.age = age
#           super().__init__("Engineer","IT","1,00,0000")


# emp1 = Employee("Software Tester","IT","2,00,000")
# emp1.showdetails()
# emp2 = Enginner("Mohit Sharma",25)
# emp2.showdetails()

#! 4

# class Order:

#      def __init__(self,item,price):
#           self.item = item
#           self.price = price

#      def __gt__(self,ord2):
#                  return self.price > ord2.price


# ord1 = Order("Chips",20)              
# ord2 = Order("Tea",10)              

# print(ord1>ord2)

#! 5

# target = random.randint(1,10)
# guess=0
# while True:
#    guess+=1
#    userChoice = input("Guess the target or Quit(Q) : ")
#    if(userChoice=="Q"):
#       break
   
#    userChoice = int(userChoice)
#    if(userChoice == target):
#       print("You guesed the number in ",guess,"times")
#       break
#    elif(userChoice > target):
#       print("Please Guess smaller number")
#    else:
#       print("Please Guess bigger number")

# print("----- Game Over ------")

#? def calc(n):

#   for i in range(n):
#      x = int(input())
#      if(x < 10):
#       print("YES")
#      else:
#       print("No")
     

# n = int(input())
# calc(n)


# def calc(n):
#     for i in range(n):
#         x,y = list(map(int,input().split()))
#         print (x*y)


# n = int(input())
# calc(n)

# inp = int(input("Enter you weight (in Pounds)"))
# kilo = inp * 0.45359237

# print(f"Your weight in kilogram is ",kilo)


num1 = int(input("Enter first number? "))
num2 = int(input("Enter second number? "))

print("Value of num1 is ",num1)
print("Value of num2 is ",num2)

temp =num1
num1=num2
num2=temp
print("Value of num1 is ",num1)
print("Value of num2 is ",num2)