# height = int(input("Enter height in feet:"))
# number = int(input("Enter the number: "))

# if(height>3):
#     print("Buy Token")
# else:
#     print("No token required")    

#     if number%2==0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")

#     #Nested if else


# age = int(input("Enter your age : "))

# if age>18:
#    if age<30:
#     print("You are young")
#    else:
#     print("You are above 30")
# else:
#    print("You are child")



year = int(input("Enter the year: "))

if year%4==0:
   if year%100==0:
       print(f"{year} is leap year.")
       if year%400==0:
        print(f"{year} is leap year.")
       else:
        print(f"{year} is leap year.")
   else:
       print(f"{year} is leap year.")
else:
   print(f"{year} is not a leap year")