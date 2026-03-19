# 1

# size = (input("What size of pizza you want (S/M/L)?"))
# bill=0

# if size=='s' or size == "S":
#     bill+=100
#     print("Price of Small Pizza is 100 Rs.")

# elif size=='m' or size == "M":
#     bill+=200
#     print("Price of Medium Pizza is 200 Rs.")
# else:
#     bill+=300
#     print("Price of Large Pizza is 300 Rs.")

# add_pepproni= input("Do you want to add pepproni (Y/n)?")
# if add_pepproni == 'y' or add_pepproni =="Y":
#     if  size=='s' or size == "S":
#         bill+=30
#     else:
#         bill+=50

# add_extra_cheese= input("Do you want to add extra cheese (Y/n)?")
# if add_extra_cheese == 'y' or add_extra_cheese =="Y":
#     if  size=='s' or size == "S":
#         bill+=20
  
# print(f"Your final bill is {bill}")  

# 2

name1= input("Enter your Full Name? ").lower()
name2= input("Enter your Lover Full Name? ").lower()
True1=0
Love2=0

name3=name1+name2
T = name3.count('t')    
R=name3.count('r')    
U=name3.count('u')    
TE=name3.count('e')     

L = name3.count('L')    
O=name3.count('o')    
V=name3.count('v')    
LE=name3.count('e')     
true = T+R+U+TE
false = L+O+V+LE
score = f'{true}{false}'
print(f"Your score is {score}%")
print(type(score))

if int(score) <40 :
    print("Your relationship is not good")

elif int (score) >40 and int (score) < 70:
    print("Your relationship is good")     

else:
    print("Your relationship is excellent")



