# Private Variable

class Hero:
    # class variable
    jumlah_hero = 0
    def __init__(self,name,health) -> None:
        self.name = name
        self.health = health
        # instance private variable
        self.__private = "private"
        # instance protected variable
        self._protected = "protected"

zilong = Hero("zilong",800)
zilong._protected = "test"
print(zilong.__dict__)
print(zilong._protected)


