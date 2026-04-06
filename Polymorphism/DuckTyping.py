class Duck:
    def swim(self):
        print("I am duck and i can swim")
    def speaks(self):
        print("Quack Quack")
class Dog:
    def swim(self):
        print("I am dog and i can swim")
    def speaks(self):
        print("Woof Woof")
class Person:
    def swim(self):
        print("I am person and i can swim")
    def speaks(self):
        print("Hi ")


class Demo:

    def display(self,obj):
        obj.swim()        
        obj.speaks()        

duck = Duck()
dog = Dog()
person = Person()
demo = Demo()
demo.display(dog)        
demo.display(duck)        
demo.display(person)        