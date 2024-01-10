class Hero:
    def __init__(self,name,health,attackpower):
        self.__name = name
        self.__health = health
        self.__attpower = attackpower
        
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    def diserang(self,attackpower):
        self.__health -= attackpower

zilong = Hero("zilong",800,350)
print(zilong.getName())
zilong.diserang(10)
print(zilong.getHealth())

