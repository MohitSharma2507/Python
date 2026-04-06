
#! What is Method Overloading?
# Same method name with different number or type of arguments within same class
# Python does NOT support true method overloading like Java ❌
# 👉 If you define multiple methods with same name → last one overrides previous


# class Demo:
#     def add(self, a, b, c=0):
#         return a + b + c
    
# d = Demo()
# print(d.add(2,3))     # 5
# print(d.add(2,3,4))   # 9    

class Demo:
    def add(self, *args):
        return sum(args)
    
d = Demo()
print(d.add(1,2))        # 3
print(d.add(1,2,3,4))    #10
print(d.add(1,2,3,4,7,8))#25   


#! What is Method Overriding?
# Child class provides its own implementation of a method already defined in parent class

class Animal:
    def sound(self):
        print("Some sound")

#! ✔ Child method replaces parent method
# class Dog(Animal):
#     def sound(self):
#         print("Bark")

#! ✔ Calls parent + child method   
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

d = Dog()
d.sound()   # Bark


# 🔥 Key Differences
# Feature	        Overloading 🔄	                       Overriding 🔁
# Definition	    Same method, different parameters	    Same method, different implementation
# Python Support	Not direct ❌                           Fully supported ✅
# Classes	        Same class	                            Parent → Child
# Example	        add(a,b) / add(a,b,c)	                sound() in Animal & Dog




     