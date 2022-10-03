import random

_f = open("udemy\eng_words.txt", "r+")
_contents = _f.readlines()

_l_words = _contents[1543: 1583]

_f.close()
def getWords():
    return _l_words[random.randint(0, 1583-1543)]
 
