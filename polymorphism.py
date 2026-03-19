# when the same operator is allowed to  have different meaning according to context.

# Operator & Dunder function

#? a+b  -->    a.__add__(b)

class Complex:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2): #Dunder function
        newReal = self.real +num2.real
        newImg = self.img +num2.img
        return Complex(newReal,newImg)

c1 = Complex(1,3)
c1.shownumber()

c2 = Complex(2,5)
c2.shownumber()

c3 = c1+c2
c3.shownumber()

