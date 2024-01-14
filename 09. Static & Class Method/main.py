class Hero:
    __jumlah = 0

    def __init__(self, name,):
        self.__name = name
        Hero.__jumlah += 1

    # getter

    def getJumlah(self):
        return Hero.__jumlah

    def getJumlah1():
        return Hero.__jumlah

    # Method static (decorator)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

# awal game
zilong = Hero("zilong")
print(f"Jumlah : {zilong.getJumlah2()}")
layla = Hero("layla")
print(f"Jumlah : {layla.getJumlah2()}")


zilong = Hero("zilong")
print(f"Jumlah : {zilong.getJumlah3()}")
layla = Hero("layla")
print(f"Jumlah : {layla.getJumlah3()}")






