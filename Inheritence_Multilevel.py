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