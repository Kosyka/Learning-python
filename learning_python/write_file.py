open_file = open("new_text.txt", "w", encoding="utf-8")
kol = 0
while kol < 3:
    text = input("Введите текст, который будет записываться в файл... \n")
    open_file.write(text)
    open_file.write("\n")
    kol += 1

open_file.close()
open_file = open("new_text.txt", "r", encoding="utf-8")
print(open_file.read())
open_file.close()


open_file = open("new_text.txt", "w", encoding="utf-8")
line = ["Hello World! \n","Строка 2\n","Строка 3\n"]
open_file.writelines(line)
open_file.close()
open_file = open("new_text.txt", "r", encoding="utf-8")
print(open_file.read())
open_file.close()