#Классово верная зверушка
#Демонстрирует атрибуты класса и статические методы
class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверушек сейчас", Critter.total)
        
    def __init__(self, name):
        print("\nПоявилась на свет новая зверушка!")
        self.name = name
        Critter.total += 1
    
#Основная часть программы
print("Нахожу значение атрибута класса Critter.total: ",end=" ")
print(Critter.total)
print("\nСоздаю зверушек")
crit1 = Critter("Сид")
crit2 = Critter("Ченуски")
crit3 = Critter("Вильям")
Critter.status()
print("\nОбращаюсь к атрибуту класса через объект: ", end=" ")
print(Critter.total)
input("Нажмите Enter, чтобы выйти...")