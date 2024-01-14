class Hero:
    __jumlah = 0

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    def getHealth(self):
        return self.__health

    @property
    def info(self):
        return "name {} : \n\thealth : {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,newArmor):
        self.__armor = newArmor


sniper = Hero("sniper",100,50)

print("Getter dan Setter")
print(sniper.__dict__)
sniper.armor = 10
print(sniper.__dict__)