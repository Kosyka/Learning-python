#Зверушка с конструктором
#Создание конструктора класса
class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("На свет появилась новая зверушка!")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "Имя: " + self.name + "\n"
        return rep
        
    def talk(self):
        print("Привет, меня зовут {0}, рад познакомиться!".format(self.name))

#Основная часть
crit1 = Critter("Dory")
crit2 = Critter("Nipon")
crit1.talk()
crit2.talk()
crit1.name = "Вильям"
crit1.talk()
print(crit1)
input("\n\nНажмите Enter...")