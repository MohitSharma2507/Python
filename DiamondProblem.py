class A:
    def display(self):
        print("display from A class")
class B(A):
    #   def display(self):
    #     print("display from B class")
    pass
class C:
    #   def show(self):
    #       print("Hi from C class")
    #   def display(self):
    #     print("display from B class")
    pass
class D(B,C):
    pass

d1 = D()
d1.display()
