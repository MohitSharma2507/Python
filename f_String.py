name = "Krishna"
age = 30
height = 1.6

print(f"My name is {name}. and i'm {age}. year old and my height is {height} meters.")



days = 90*365
weeks = 90*52
months = 90*12

age = int(input("What is your age? "))

year_left = 90-age
calc_days = year_left*365
# calc_days = days - age*365
calc_weeks = year_left*52
# calc_weeks = weeks - age*52
calc_months = year_left*12
# calc_months = months -age*12

print(f"You have {calc_days} daysm,{calc_weeks} weeks and {calc_months} month left")