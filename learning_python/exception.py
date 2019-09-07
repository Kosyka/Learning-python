#Перехват исключения с помощью try/excep

try:
    a = int(input("Введите целое число: "))
except ValueError as e:
    print("Ошибка типа! {}".format(e))
else:
    print("Вы ввели {0}, спасибо!".format(a))

input("Для выхода нажмите Enter...")