import random

lett = int(input("How many letters would you like in your password? : "))
syb=int(input("How many symbol would you like? : "))
num=int(input("How many number would you like? :"))


numbers=['0','1','2','4','5','6','7','8','9']
sybmols=['%','!','@','#','$','^','&','*','(',')',"_","=",'+']
letter=['a','b','c','d','e','f','g']

list1=[]

for i in range(lett):
    random.shuffle(letter)
    list1.append(letter[i])
for i in range(syb):
    random.choice(sybmols)
    list1.append(sybmols[i])
for i in range(num):
    random.shuffle(numbers)
    list1.append(numbers[i])

# result = ''.join(map(str, list1))
# print(result)

result=""
for i in list1:
   result += i

print(result)   
