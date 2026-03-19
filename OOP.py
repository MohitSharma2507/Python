
#* To map with real world scenario , we started using objects in code.

#! Created Class
# class car:
#      color:"blue"
#      brand:"mercedes"

# car1 = car() #! Created object
# print(car1.color)
# print(car1.brand)

#! Constructor

#* All classes have a function called _init_(), which is always executed when the object is being initiated.

class student:
    name = "Mohit"
    #!    default constructor
    def __init__(self):
        print("Calling constructor..")

    #!    parameterized constructor
    def __init__(self,fullname,marks):
        self.name = fullname 
        self.marks = marks

s1 = student("Ankit",97)
print(s1.name)
print(s1. marks)

