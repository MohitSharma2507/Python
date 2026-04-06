# Dunder methods (Double UNDERscore methods) are special methods in Python that start and end with __ (e.g., __init__, __str__).
# 👉 Python automatically calls them to perform built-in operations.

#! _str__ → String Representation (User-friendly)

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"

s = Student("Mohit")
print(s)

#! __repr__ → Developer Representation [✔ Used for debugging]

# def __repr__(self):
#     return f"Student('{self.name}')"

#! __len__ → Length
# class MyList:
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):
#         return len(self.data)

# obj = MyList([1,2,3,4])
# print(len(obj))   # 4

#! __eq__ → Equality (==)
# class Person:
#     def __init__(self, age):
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

# p1 = Person(25)
# p2 = Person(25)

# print(p1 == p2)   # True

#! __lt__ → Less Than (<)
# def __lt__(self, other):
#     return self.age < other.age

#! __getitem__ → Indexing
# class MyList:
#     def __init__(self, data):
#         self.data = data

#     def __getitem__(self, index):
#         return self.data[index]

# obj = MyList([10,20,30])
# print(obj[1])   # 20

#! __call__ → Make Object Callable
# class Demo:
#     def __call__(self):
#         print("Object is called like a function")

# d = Demo()
# d()   # works like function

#! __del__ → Destructor
# def __del__(self):
#     print("Object destroyed")
# # ✔ Called when object is deleted