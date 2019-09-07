#Консервация данных и деконсервация
#Демонстрирует консервацию данных и доступ к ним через интерфейс полки
import pickle, shelve
#Модуль pikle_it позволяет консервировать структуры и сохранять их в файл
#Модуль shelve обеспечивает произвольный доступ к консервированным структурам

line_1 = ["это первый список \n","Для консервации 1\n","Строка 3 списка 1\n"]
line_2 = ["это второй список \n","Для консервации 2\n","Строка 3 списка 2\n"]
line_3 = ["это третий список \n","Для консервации 3\n","Строка 3 списка 3\n"]

file = open("pickles1.dat", "wb") # .dat хранение данных в двоичном формате
#Консервация структур методом dump(данные, файл)
pickle.dump(line_1, file)
pickle.dump(line_2, file)
pickle.dump(line_3, file)
file.close()

#Чтение и расконсервация из файла методом load(file)
file_1 = open("pickles1.dat", "rb")
line1 = pickle.load(file_1)
line2 = pickle.load(file_1)
line3 = pickle.load(file_1)

print(line1,"\n", line2, "\n", line3)



#модуль shelve, полки
#создадим полку
s = shelve.open("pickles2.dat")
#Помещаем списки на полку, полки очень похожи на словари, есть ключ и значение (причем ключ может быть только строкой)
s["line1"] = ["это первый список \n","Для консервации 1\n","Строка 3 списка 1\n"]
s["line2"] = ["это второй список \n","Для консервации 2\n","Строка 3 списка 2\n"]
s["line3"] = ["это третий список \n","Для консервации 3\n","Строка 3 списка 3\n"]
#Вызываем метод sync()
s.sync() #Убедимся, что данные записаны

#Извлекаем список из полки
print("\nИзвлекаем из файла полки\n")
print("Это первый список полки: ", s["line1"], "\n")
print("Это второй список полки: ", s["line2"], "\n")
print("Это третий список полки: ", s["line3"], "\n")
#Закроем файл:
s.close()
input("\n\nНажмите Enter...")
