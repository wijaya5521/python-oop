''' Method ada dua : 
1. Method interaksi antar object
2. Method interaksi dengan client
'''

class Hero():
    # class variabel
    jumlah_hero = 0
    
    def __init__(self,name,health,power,armor):
        self.name = name
        self.health = health
        self.power = power
        self.aromor = armor
        Hero.jumlah_hero += 1
        
    # void function, method tanpa return tanpa argumen
    def siapa(self):
        print("namaku adalah " + self.name)
        
    # method dengan return tanpa argumen
    def healthUp(self,health_up):
        self.health += health_up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Zilong",800,300,150)
hero2 = Hero("Layla",700,350,120)

hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())

        
