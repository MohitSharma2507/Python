# Single Inheritance

class Car:

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stoping...")    

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")        
car2 = ToyotaCar("Prius")    

print(car1.start())
print(car1.stop())

# Multi-level Inheritance

class Car:

    @staticmethod
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand   

class fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

Car1 = fortuner("diesel")        
Car1.start()

# Multiple Inheritance

class A:
    varA = "Welcome to class A"

class B:
   varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)