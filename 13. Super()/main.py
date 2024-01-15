class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def showInfo(self):
        print("{} dengan health : {}".format(self.__name,self.__health))

class Hero_intelegent(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name,100)
        super().__init__(name,100)
        super().showInfo()

class Hero_stength(Hero):
    def __init__(self, name):
        super().__init__(name,200)
        super().showInfo()

lina = Hero_intelegent('lina')
axe = Hero_stength('axe')

print(lina.getName(), "", lina.getHealth())
print(axe.getName(), "", axe.getHealth())