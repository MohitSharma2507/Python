# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f"Are you from {dept} deartment?")

# # greet("Mohit","CS",)     #positional argument
# # greet(dept="CS",name="Mohit")     #keyword argument
# greet("CS",dept="Mohit")     #1st positional , 2nd keyword argument

# -------------------------------------------------------------------------------

# Default Argument

# def greet(name,dept="CS"): #Default argument should be on last should follow positional argument
#     print(f"Hi {name}")
#     print(f"Are you from {dept} deartment?")
# greet("Mohit","BTECH")

# -------------------------------------------------------------------------------

# Arbitrary Positional Argument
# def sum(*numbers):
#     c=0
#     for i in numbers:
#         c=c+i
#     print(f"Sum = {c}")

# sum(2,3)
# sum(2,3,4)
# # sum(2,3,4,"jenny")

# 1. Arbitrary Keyword Argument
# def sum(name, *numbers):#better to assign postional arg first then keyword arg
#     c=0
#     print(numbers)
#     print(name)
#     for i in numbers:
#         c=c+i
#     print(f"Sum = {c}")

# # sum(2,3)
# # sum(2,3,4)
# sum("jenny",2,3,4)

# 2. Arbitrary Keyword Argument
def info_person(**data):
    # print(data)

    for key,val in data.items():
        print(key,val)


info_person(name="Mohit",age=25,dept="CSE")
info_person(name="Rohit",age=30,dept="civil")
info_person(name="Jai",age=26,dept="Defence")
info_person(name="Ankit",age=28,dept=" CA")


def info_person(*args, **data):
    # print(data)
    print(args)

    for key,val in data.items():
        print(key,val)


info_person(1,2,name="Mohit",age=25,dept="CSE")
info_person(3,4,name="Rohit",age=30,dept="civil")
info_person(5,6,name="Jai",age=26,dept="Defence")
info_person(6,7,name="Ankit",age=28,dept=" CA")


#def func(Normal arg, arb positional arg, arb Keyword arg):

# func(Normal arg, arb positional arg, arb Keyword arg)