import math


# def func(Wall,height,weight):
#    No_of_can = (height*weight)/Wall
#    print(math.ceil(No_of_can)) 

# Wa = int(input("Size of the wall in sq./m : "))
# he= int(input("Height of the wall : "))
# we= int(input("Weight of the wall : "))
# func(height=he,Wall=Wa,weight=we)

#PRIME NUMER

# def is_prime(num):
#   is_prime = True
#   i=1
#   for i in range(2,num-1):
#        if num%i==0 :
#            is_prime=False
#            break
       
#   if(is_prime):
#       print(f"{num} is PRIME")        
#   else:
#       print(f"{num} is NOT Prime")


# num=int(input("Enter the number : "))

# is_prime(num)


def leap_year(year):
    if year % 4 ==0:
        if year% 100 == 0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calc_days(year,month):

   days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
   if leap_year(year) and month == 2:
      return 29
   else:
      return days_list[month-1]

year=int(input("Enter year : "))
month = int(input("Enter month : "))

print(calc_days(year,month))