# 1. for i in range(1, 20, 2):  # start=1, stop=20, step=2
#     print(i, end = " ")

# sum=0
# for i in range(1,101):
#     if i%2==0 :
#       sum+=i
    
# print(f"Sum of even number is {sum} ")    

for i in range(1,100):

    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")  
    elif i%3==0 :
        print("Fizz")    
    else:
        print(i)    

