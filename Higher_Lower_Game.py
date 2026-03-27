import Higher_game_DB
import random
import os

def display_accountInfo(account):
    name= account['name']
    desc =account['description']
    country=account['country']
    follower=account['followers_count']
    return (f"{name} a {desc}, from {country}")

is_True=True
score=0
while is_True:
    account1=random.choice(Higher_game_DB.data)
    account2=random.choice(Higher_game_DB.data)

   
    print(f"Compare 1 : {display_accountInfo(account1)}")
    print(f"Compare 2 : {display_accountInfo(account2)}")

    if account1['name'] is not account2['name']:

        user_inp=int(input("Who has more followers? Type '1' or '2' :"))

        if account1['followers_count']>account2['followers_count'] and user_inp == 1:
            score+=1
            os.system("cls")
            print(f"You are right, Your Score is {score}")

        elif account1['followers_count']<account2['followers_count'] and user_inp == 2:
            score+=1
            os.system("cls")
            print(f"You are right, Your Score is {score}")
        elif account1['followers_count']<account2['followers_count'] and user_inp == 1:
            print(f"You are wrong, Your Final Score is {score}")
            is_True=False
        elif account1['followers_count']>account2['followers_count'] and user_inp == 2:
            print(f"You are wrong, Your Final Score is {score}")
            is_True=False
