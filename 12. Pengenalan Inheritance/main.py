class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_intelegent(Hero):
    pass

class Hero_strength(Hero):
    pass


lina = Hero('lina',100)
sandy = Hero_intelegent('sandy',80)
axe = Hero_strength('axe',200)

print(lina.name)
print(sandy.__dict__)
print(axe.__dict__)