# A class method is bound to the class & receives the class as an implicit first arguments
#! Note = static method can't access or modify class rate & generally for utility.

class Person:
    name = "anonymous"

    # def changename(self,name):
    #     Person.name = name
    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Mohit Sharma")          

print(Person.name)
print(p1.name)
