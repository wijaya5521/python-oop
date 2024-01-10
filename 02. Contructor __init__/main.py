# __init__ is code running first each object of class called

class Hero:
    def __init__(self,name,health,):
        self.name = name
        self.health = health
        
hero1 = Hero("Zilong",800)
hero2 = Hero("Layla",700)
 
print("-------------------------")
print("Hero 1")
print(f"Hero name : {hero1.name}")            
print(f"Health : {hero1.health}")
print("-------------------------")
print("Hero 2")
print(f"Hero name : {hero2.name}")            
print(f"Health : {hero2.health}")
