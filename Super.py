# Super() method is used to to access methods of the parent class

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
       print("Car Started...")

           
    @staticmethod
    def stop():
       print("Car Stoping...")

class ToyotaCar(Car):

    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
               
car1 = ToyotaCar("fortuner","petrol")
print(car1.type)               