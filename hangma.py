import random
from intro import stages, logo
import random_Words
import os


print(logo)
life = len(stages) - 1
word_list = random_Words.word_list
chosen_word = random.choice(word_list)
display = ["_" for i in chosen_word]
a = random.randint(0, len(chosen_word) - 1)
display[a] = chosen_word[a]


print(display)
print(stages[life])
while "_" in display and life != 0:
    inpute = input("say smthing: ")
    
    os.system('cls')
    
    if inpute in display:
      print("you have already guessed")
      print(display)
      continue
    
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == inpute:
        display[position] = inpute

    if inpute not in chosen_word:
        life-=1
        print(stages[life])
        print("try again \t life remaining: ", life)
    
    # os.system("cls")
    print(" ".join(display))

if life == 0:
  print("try again later")
  print("the correct word was: " + chosen_word)
else:
    print("well done")
