# when a function call itself repeatedly

#? Print n to 1 backward

# def fuc(n):
#     if(n<=10):
#         print("hi")
#         fuc(n+1)
#         print(n)

# n=1
# fuc(n)


#? Print factorial

# def factorial(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#       return num * factorial(num-1)
    

# print(factorial(4)) 

#? Write a program to calculate sum of first n natural number

def sum_num(num):
    i=1
    sum=0
    if(i==num):
        return
    else:
        sum+=sum_num(num)

print(sum_num(10))

