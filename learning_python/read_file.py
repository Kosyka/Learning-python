#Открываем файл
open_file = open("text.txt", "r", encoding="utf-8")
print(open_file.read())
open_file.close()

open_file = open("text.txt", "r", encoding="utf-8")
print(open_file.readline())
print(open_file.readline())
print(open_file.readline())
open_file.close()

open_file = open("text.txt", "r", encoding="utf-8")
text_s  = open_file.readlines()
print(text_s)
open_file.close()