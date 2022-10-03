import random
import extractWords


life = 3
word = extractWords.getWords()
new_word =  ["_" for i in range(len(word))]

def generateQuiz():
    temp = list(word)
    a = random.randint(1, len(temp) - 1) #2
    for item in range(a):
     pos_c = random.randint(0, len(temp) - 1)
     temp[pos_c] = "_"
    
    
    return temp
    
    
new_word = generateQuiz()
print("".join(new_word))



def getInputAndCheck_v2(life):
    #"aardvark" .... "__r_dva_k"
    while life != 0 and new_word.count("_") > 0:
      print("life remaining: ", life)
      inp = input("get input: ")
      i = False
      item = 0
      for item in range(0, len(new_word)):
       if word[item] == inp and new_word[item] == "_":
         i = True
         break
      
      if i == True:
        new_word[item] = inp
      else:
          life-=1 
      print("".join(new_word))
    
    return life

a = getInputAndCheck_v2(life)

if a != 0:
  print("well done")
else:
    print("lol xd peasant")
    

    
        
    
    