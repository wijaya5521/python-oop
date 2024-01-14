class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self,name,health,setPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = setPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.healthMax = self.__healthStandar * self.__level
        self.attPower = self.__attPowerStandar * self.__level
        self.armor = self.__armorStandar * self.__level

        self.health = self.healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} : \n \thealth = {}/{}" \
               "\n\tpower : {}" \
               "\n\tarmor : {}" \
                "\n\texp : {}" \
               "\n\tlevel : {}".format(self.__name,self.health,self.healthMax,self.attPower,self.armor,self.__exp,self.__level)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp = addExp
        if self.__exp >= 100:
            print(self.__name,'level up')
            self.__level += 1
            self.__exp -= 100
            self.healthMax = self.__healthStandar * self.__level
            self.attPower = self.__attPowerStandar * self.__level
            self.armor = self.__armorStandar * self.__level
            self.health = self.healthMax

            print(alucard.info)

    def serang(self,power):
        self.gainExp = power

alucard = Hero("alucard",100,5,10)

print(alucard.info)
alucard.serang(100)
alucard.serang(50)
