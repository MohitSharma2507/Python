import random 
import words_file  

print("Lets Play Hangman Game!!")
 
random.shuffle(words_file.words)
word = words_file.words[0].lower()

length = len(word)
list2 = list(word)

print(f"You have {length} lives. Guess the word!")

list3=['_']*length
print(list3)

lives = length

while lives > 0 and "_" in list3:
    guess = input("Guess a letter: ").lower()
    if guess in list2:
          for i in range(len(list2)):
            if list2[i] == guess:
                list3[i] = guess
                
          print(list3)
    else:
          lives -= 1
          print("Wrong guess!")
          print("Lives left:", lives)
        
if "_" not in list3:
    print("🎉 You Win! The word was:", word)
else:
    print("❌ You Lose! The word was:", word)

