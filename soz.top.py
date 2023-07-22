import random

words = ["ona", 'ota', 'bola', 'suv', 'aka', 'daraxt', 'piyoz', 'oila', 'mars_it', 'ustoz', 'vazifa', "o'quvchi"]

random_word = random.choice(words)

while True:
    user_word = input("So'zni taxmin qiling: ")
    
    if user_word == random_word:
        print("Tabriklayman! Siz to'g'ri javobni topdingiz.")
        break
    elif user_word > random_word: 
        print("Kiritgan so'z kichikroq.")
    else:
        print("Kiritgan so'z kattaroq.")
