# Рекорды
# Демонстрация списка и его методов

scores = [] # пустой список
choise = None

while choise != '0':
    print(
        """
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        3 - Удалить рекорд
        4 - сортировать список 
        """
    )
    choise = input("Ваш выбор: ")
    
    #выход
    if choise == "0":
        print("Вы вышли!")
        input("Нажмите Enter, чтобы закрыть...\n")
    elif choise == "1":
        print("Рекорды:")
        for i in scores:
            print(i)
    elif choise == "2":
        score = input("Введите рекорд: ")
        scores.append(score)
    elif choise == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат ", score, " не содержиться в списке рекордов!")
    elif choise == "4":
        scores.sort(reverse=True)
    else:
        print("Такого пункта нет!")