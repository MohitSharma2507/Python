# <var> = <val1> if <condition> else <val2>

# food = input("food : ")
# eat = "yes" if food == "cake" else "no"
# print(eat)

# # <stt1> if <condition> else <stt2>

# food = input("food : ")
# print("sweet ") if food == "cake" or food == "jalebi" else print("not sweet")

# --------------------------------------------


# CLEVER if/Ternory Operator

age = int(input("age : "))
vote = ("false_condition","true_condition") [age < 18]
print(vote)

sal= float(input("salary : "))
tax = sal*(0.1,0.2) [sal>=50000] #?if this condition true 0.2% will calculate otherwise 0.1%
print(tax)                                                                                                                                                                                                                                       