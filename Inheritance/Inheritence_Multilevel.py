# class Human:
#     def __init__(self,num_heart):
#         print("Calling human constructor")
#         self.eyes=2
#         self.heart= num_heart
#     def eat(self):
#         print("I can eat...")     
#     def work(self):
#         print("I can work...")    

# class Male(Human):
   
#    def __init__(self,name):
#      super().__init__(1)
#      print("Calling male constructor")
#      self.name=name

#    def sleep(self):
#         print("I can sleep whole day...")   

# class Boy(Male):        
#     def sleep(self):
#         super().__init__()
#         print("I can code..")

# boy_1=Boy("Mohit")    
# print(boy_1.heart)
# print(Boy.mro())

class Human:
    can_breath=True
    def __init__(self,num_heart):
        print("Calling human constructor")
        self.eyes=2
        self.heart= num_heart
    def eat(self):
        print("I can eat...")     
    def work(self):
        print("I can work...")    

class Male(Human):
   
   def __init__(self,name):
     print("Calling male constructor")
     self.name=name

   def sleep(self):
        print("I can sleep whole day...")   

class Boy(Male):        
    def __init__(self):
        Human.__init__(self,1)
        Male.__init__(self,"Mohit")
        print("I can code..")

boy_1=Boy()    
print(boy_1.name)
print(boy_1.heart)
print(boy_1.can_breath)
print(Boy.mro())


class Human:

    def __init__(self,name,age):
       print("Calling Human constructor")
       self.name=name
       self.age=age
    def showDetails(self):
        print(f"name : {self.name}, age: {self.age}")
           

class Male(Human):
    def __init__(self,m_name,age,location):
        print("Calling Male constructor 1")
        Human.__init__(self,m_name,age)
        print("Calling Male constructor 2")
        self.location=location
    def sleep(self):
        print("I can sleep whole day...")      
        
class Female(Human):  
    def __init__(self):
      Male.__init__()
    def work(self):
        print("I can code...")      

# female_1 = Female("Mohit",20,"delhi")  
# female_1.name
# female_1.age 
male_1 = Male("Mohit",20,"delhi")   
print(Male.mro())
male_1.name
male_1.age