import os
# student_marks ={
#     "Mohit":80,
#     "Ankit":70,
#     "Jai":100,
#     "Rohit":99.5,
#     "Rajender":60,
#     "Tanishq":27
#     }

# student_grade = dict()

# for i in student_marks:
#    marks=student_marks[i]
#    if marks>90:
#       student_grade[i]='A+'
#    elif marks >80 and marks<= 90:
#        student_grade[i]='A'  
#    elif marks >70 and marks<= 80:
#        student_grade[i]='B+'  
#    elif marks >60 and marks<= 70:
#        student_grade[i]='B'  
#    else:
#        student_grade[i]='C'  

# print(student_grade)     

def find_winner(bidder):
    max=0
    name=""
    for i in bidder:
        if max < bidder[i]:
         max=bidder[i]
         name=i
    print(f"Here is the list of all the bidders : ",bidder.keys())
    print(f"The winner is {name} with a bid of {max}")


is_Bid=True
bidder={}

while is_Bid:

    name=input("What is your name? ")
    price=int(input("What is your Bid? "))

    bidder[name]=price

    is_bidder=input("Are there any other bidders? ")

    if is_bidder=="no"or is_bidder=="No" or is_bidder=="NO":
      is_Bid=False
      find_winner(bidder)
    elif is_bidder=="yes"or is_bidder=="Yes" or is_bidder=="YES":
      os.system('cls')