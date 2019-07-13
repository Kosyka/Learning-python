# Анаграммы
# Компьютер выбирает какое-либо слово и характеристически переставляет его буквы
# Задача игрока - восстановить исходное слово

import random
# массив слов, буквы которых мы будем мешать
WORDS = (
    "дурочка",
    "курочка",
    "кинолог"
)
# Выбираем случайным образом слово (Функция choice)
word_random = random.choice(WORDS)
correct = word_random #Переменная для дальнейшего сравнения
#создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
#jumble = ""

#while word_random:
    #position = random.randrange(len(word_random))
    #jumble += word_random[position]
    #word_random = word_random[:position] + word_random[(position+1):]
word_random = [i for i in word_random]
random.shuffle(word_random)

print("""
Добро пожаловать в игру 'Анаграммы', попробуйте отгадать загаданное слово: {0}
""".format(word_random))

guess = input("\n Попробуйте отгадать слово...")
while (guess != correct) and (guess != ""):
    print("Не правильно!\n")
    guess = input("\n Попробуйте отгадать слово...")

print("Спасибо за игру!")
input("\nЧтобы закрыть, нажмите Enter...")