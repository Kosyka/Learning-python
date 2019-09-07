#Закрытая зверушка
#Демонстрирует закрытые переменные и методы
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mod):
        print("На свет появляется новая зверушка!")
        self.name = name
        self.__mod = mod
    
    def talk(self):
        print("\nМеня зовут {0}", self.name)
        print("\nСейчас я чувствую себя {0}", self.__mod)

#Главная программа
crit1 = Critter(name = "Бобик", mod = "Прекрасно")
crit1.talk()
print(crit1._Critter__mod)