class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def showInfo(self,tipe):
        print("{} dengan health : {}".format(
            self.getName(),
            self.getHealth()
            )
        )

class Hero_intelegent(Hero):
    def __init__(self, name):
        super().__init__(name,100)

    def showInfo(self):
        print("{} \n\t Tipe : intelegent\n\t Health : {}".format(
            self.getName(),
            self.getHealth()
            )
        )

class Hero_stength(Hero):
    def __init__(self, name):
        super().__init__(name,200)

lina = Hero_intelegent('lina')
axe = Hero_stength('axe')

lina.showInfo()