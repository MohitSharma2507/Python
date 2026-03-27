# when the same operator is allowed to  have different meaning according to context.

# Operator & Dunder function

#? a+b  -->    a.__add__(b)

# class Complex:

#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2): #Dunder function
#         newReal = self.real +num2.real
#         newImg = self.img +num2.img
#         return Complex(newReal,newImg)

# c1 = Complex(1,3)
# c1.shownumber()

# c2 = Complex(2,5)
# c2.shownumber()

# c3 = c1+c2
# c3.shownumber()


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()