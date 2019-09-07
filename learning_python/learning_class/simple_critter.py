#Просто зверушка
#Демонстрация простого класса и объекта
class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет, я зверушка - экземпляр класса Critter")

#Основная часть
crit = Critter()
crit.talk()
input("\n\nНажмите Enter...")
