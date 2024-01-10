# 01. Introduction to Object Oriented Programming

'''
Object Oriented Programming (OOP) is other style to write code
There is two style we write code :
1. Sturctural or Procedural Programming
2. Object Oriented Programming (OOP)

- Procedural Programming is code that read from top to bottom
- OOP read code based on object and it relation not read from top to bottom
'''

# Study case "Hero in mobile game"
class Hero:
    pass

hero1 = Hero()
hero2 = Hero()

hero1.name = "Zilong"
hero2.name = "Layla"

hero1.health = 100
hero2.health = 80

print(hero1.name)
print(hero1.health)
print(hero2.name)
print(hero2.health)