# Used to delete object properties or object itself

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# s1 = Student("Mohit Sharma",34)
# del s1.name

""" del s1
 !print(s1.name)
 !print(s1.age)
 !print(s1) 
"""

# Private Specifier

class Person:
    __name = "Mohit"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())


