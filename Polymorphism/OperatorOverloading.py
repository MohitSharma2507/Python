# Operator overloading means giving special meaning to operators when used with objects.
# Same operator behaves differently depending on the data type.

# class ComplexNumber:

#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
    
#     def __add__(self, other):
#         return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"

# c1= ComplexNumber(1,2)   
# c2= ComplexNumber(3,4)   

# print(c1+c2)

class Paybill:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __gt__(self, other):
        if self.age>other.age:
            return True
        else:
            return False

c1= Paybill("Mohit",2)   
c2= Paybill("Rohit",29)   

if c1>c2:
    print(f"{c1.name} is going to pay the bill")
else:
    print(f"{c2.name} is going to pay the bill")    
