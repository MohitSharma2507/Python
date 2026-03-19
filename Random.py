import random

# a= random.randint(1,3) # 1 and 3 both are included
# a= random.randrange(1,3) # 3 not included
# a= random.random() # return floating number btwn [0.0 to 1.0] 1.0 not included
# a= random.uniform(1,3) # return floating number btwn given range

# l=[10,23,45,29,59]
# a= random.choice(l)

# l=[10,23,45,29,59]
# random.shuffle(l) # return 
# print(l)

# l=[1,0]
# coin= random.choice(l)
# if coin==1:
#     print("Heads")
# else:
#     print("Tails")

# side=random.randint(0,1) 
# if side==1:
#     print("Heads")
# else:
#     print("Tails")

names = input("Enter names separated by space: ").split(",")
length= len(names)
choose=random.randint(0,length-1)
print(f"{names[choose]} will pay the bill")