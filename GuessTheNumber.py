import random
import logo_art


def game():
   print(logo_art.logo)
   print("let me think of a number between 1 and 50")
   level=int(input("Enter the level of difficulty: 1, 2 or 3: "))
   chances = 0
   if level == 1:
      chances = 10
   elif level == 2:
      chances = 7 
   elif level == 3:
      chances = 5 


   computer_guess=random.randint(1,50)
   is_guess=False
   i=1
   while i<=chances:
      guess_num=int(input("Make a guess : "))
      if guess_num==computer_guess:
         print(f"You guessed it right.The number is {computer_guess}")
         is_guess=True
         break
      elif guess_num>computer_guess:
         print(f"Your guess is too high. Guess Smaller number")
      elif guess_num<computer_guess:
         print(f"Your guess is too Low. Guess Bigger number")
         
      i+=1

   if is_guess == False:
      print("You failed to guess the number")

game()