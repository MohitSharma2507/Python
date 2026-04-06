class University:
   def __init__(self, name):
        self.uni_name = name

   def showDetails(self):
        print("Display from university class")


class Branch(University):
   def __init__(self, name, branch):
        super().__init__(name)
        self.branch_name = branch

   def showDetails(self):
        print("Display from branch class")


class Course(University):
   def __init__(self, name, course,branch):
        super().__init__(name,branch)
        self.course_name = course

   def showDetails(self):
        print("Display from course class")


class Student(Course, Branch):
   def __init__(self, uni, branch, course, student):
        super().__init__(uni, course,branch)   # follows MRO
        self.branch_name = branch       # manually set
        self.stu_name = student

   def showDetails(self):
        print("Display from student class")


stu_1 = Student("DU", "CSE", "Python", "Mohit")

print(stu_1.course_name)
print(stu_1.branch_name)
print(stu_1.stu_name)
print(stu_1.uni_name)

stu_1.showDetails()
print(Student.mro())