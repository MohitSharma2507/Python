class Student:
    def __init__(self,name,rollno,age):
        self.name = name #public instance variable
        self._rollno =rollno #protected instance variable
        self.__age = age #private instance variable
    def display(self):
        print(f"Hi I'm {self.name} roll no {self._rollno} from student class")   

class Branch(Student):
    pass


s1= Student("Mohit",21,23)
s1.display()
print(s1._Student__age) #mangling to acess private attribute outside class