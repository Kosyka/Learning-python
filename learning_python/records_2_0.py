#Рекорды 2.0
#Вложенные последовательности

scores = []
choice = None

while choice != "0":
    print("""
        Рекорды 2.0:
        0 - выйти
        1 - показать рекорды
        2 - добавить рекорд
    """)
    choice = input("Ваш выбор: ")
    print()
    #выход
    if choice == "0":
        print("До свидания!")
    
    #вывод результата
    elif choice == "1":
        print("Рекорды \n")
        print("Имя\tРезультат")
        for entry in scores:
            name, score = entry
            print(name, "\t", score)
    #add a score   
    elif choice == "2":
        name = input("Впишите Имя: ")
        score = int(input("Впишите его рекорд: "))
        entry = (name, score)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # Список из 5 рекордов
    else:
        print("Извините, но в меню нет такого пунка")

input("\n\n Введите Enter для выхода...\n\n")