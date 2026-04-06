# # class Human:
# #    def eat(self):
# #       print("I am eating...")
# #    def work(self):
# #       print("I am working...")


# # class Male:
# #    def flirt(self):
# #       print("I am flirting...")

# #    def work(self):
# #       print("I am coding...")

# # class Boy(Human,Male):
# #     #  def work(self):
# #     #   Human().work()
# #     #   print("I am just boy...")
# #     pass

# # boy_1 = Boy()
# # boy_1.flirt()
# # boy_1.eat()
# # boy_1.work() # will access work() of human because (Human,Male) human is first
# # Human.work(boy_1) # will access work() of Male 


# class Human:
#    def __init__(self,num_heart):
#       print("calling init from human")
#       self.num_eyes=2
#       self.num_nose=1
#       self.num_heart=1

#    def eat(self):
#       print("I am eating...")

#    def work():
#       print("I can work..")
# class Male:
#    def __init__(self,name):
#       print("calling init from Male")
#       self.name=name

#    def flirt(self):
#       print("I am flirting...")

# # Call both parent constructors
# class Boy(Male, Human):
#     def __init__(self, name,language,num_heart):

#         Human.__init__(self,num_heart)
#         Male.__init__(self, name)

#         self.language=language
#     def lang(self):
#        print(self.language)

   
# boy_1 = Boy("Mohit","python",1)
# print(boy_1.num_eyes)
# print(boy_1.name)
# print(boy_1.num_heart)
# boy_1.lang()
# print(Boy.mro())
# # print(boy_1.num_eyes)


class LoggerMixin:
    def log(self):
        print("Logging...")

class App(LoggerMixin):
    pass


