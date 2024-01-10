class Hero:
    jumlah_hero = 0
    
    def __init__(self,name,health,power,armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        
    def getHealth(self):
        return self.health
    
    def serang(self,enemy):
        print(f"{self.name} menyerang {enemy.name} dengan power {self.power}")
        enemy.diserang(self,self.power)
        
    def diserang(self,enemy,enemypower):
        print(self.name + ' diserang ' + enemy.name)
        attack_received = enemypower - self.armor
        print("Serangan terasa : " + str(attack_received))
        
zilong = Hero("zilong",800,300,150)
layla = Hero("layla",700,450,120)

zilong.serang(layla)

