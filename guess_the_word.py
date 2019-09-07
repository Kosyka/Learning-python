# Отгадай слово

import random

word = ( # Кортеж слов
    "слово",
    "книга",
    "флешка",
    "программирование",
    "интерес",
    "вселенная"
)
print("Добро подаловать, попробуйте отгадать слово. У Вас будет 5 попыток, вы должы отгадывать буквы. Удачи!!! \n")

status = True
while status:
    item = random.randrange(0,len(word))
    correct = word[item];
    i = 0
    word_used = word[item]
    word_used = [i for i in word_used]
    word_rand = random.randrange(0, len(word_used))

    guessed = [word_used[word_rand]]
    #while i < len(word_used):
     #   if guessed[0] in word_used[i]:
      #      print(guessed,end=" ")
       #     i+=1
        #else:
         #   print("#",end=" ")
          #  i+=1
    print("\n Введите букву:")
    letter = input()