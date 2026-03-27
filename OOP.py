
#* To map with real world scenario , we started using objects in code.

#! Created Class
# class car:
#      color:"blue"
#      brand:"mercedes"

# car1 = car() #! Created object
# print(car1.color)
# print(car1.brand)

#! Constructor

#* All classes have a function called _init_(), which is always executed when the object is being initiated.

# class student:
#     name = "Mohit"
#     #!    default constructor
#     def __init__(self):
#         print("Calling constructor..")

#     #!    parameterized constructor
#     def __init__(self,fullname,marks,,age=18): #defaut value age=18
#         self.nme = fullname 
#         self.marks = marks

# s1 = student("Ankit",97)
# print(s1.nme)
# print(s1.name)
# print(s1. marks)


# class Student:
#     school="DC Arya School"

#     # def __init__(self,name):
#     #     self.name = name

#     def __init__(self,name):
#         self.name = name

# s1 = Student("Mohit")
# s2 = Student("Rohit")

# print(s1.name,s1.school)


# class Student:

#     subject_name="JAVA"
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address

#     def display(self,subject_name):
#         self.subject_name=subject_name
#         print(f"Hi, I am {self.name} and i teach {subject_name}")  
#         print(f"Hi, I am {self.name} and i teach {self.subject_name}")   #error
      

# S1 = Student("Mohit","Delhi")    
# S1.display("Python")
# print(S1.subject_name)

# class Student:

   
#     def func(self):
#        print('hello')

#     def __init__(self):
#      self.func()
     

# S1 = Student()  

# del S1 #delete the object


# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     return "Hello, " + self.name

#   def welcome(self):
#     message = self.greet()
#     print(message + "! Welcome to our website.")

# p1 = Person("Tobias")
# # del p1.name    #Delete properties/attributes
# p1.welcome()



class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()