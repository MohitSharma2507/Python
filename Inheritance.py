# Single Inheritance

class Human:
    a=5

    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
        print("Parent constructor")

    def eat(self):
        print("I can Eat")

    def work(self):
        print("I can work")    

class Male(Human):

    def __init__(self):
        super().__init__()
        print("Child constructor")
    @staticmethod
    def flirt():
        print("I can flirt")  

    def work(self): #method overriding
        super().work() #access parent methods
        print(super().a) #acess parent attribute/properties
        # print(super().num_eyes)
        print("I can code")     


male_1 = Male()
male_1.eat()           
male_1.flirt()           
male_1.work()  
print(male_1.num_eyes)      
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