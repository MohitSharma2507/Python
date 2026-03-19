# Block of statement that perform a specific task


def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*= i
    return fact

n=5
print(f"factorial of {n} is " ,cal_fact(5))      


def odd_even(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")


odd_even(4)