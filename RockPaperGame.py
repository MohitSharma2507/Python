import random

game_images = ['rock', 'paper', 'scissors']

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number, you lose.")
else:
    print("You chose:", game_images[user_choice])

    comp_choice = random.randint(0, 2)
    print("Computer chose:", game_images[comp_choice])

    if user_choice == comp_choice:
        print("It's a draw")
    elif user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose!")
    elif comp_choice > user_choice:
        print("You lose!")
    elif comp_choice < user_choice:
        print("You win!")

        