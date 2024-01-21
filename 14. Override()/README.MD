## Apa Itu Overriding?
 **Overriding** adalah sebuah fitur dalam konsep object oriented programming (OOP) untuk melakukan penimpaan dari fungsi yang telah didefinisikan sebelumnya

## Cara Melakukan Overriding

Misal kita mempunyai dua kelas, yaitu kelas Kendaraan dan kelas Mobil yang mana :
- **Kelas Kendaraan** adalah kelas induk
- **Kelas Mobil** adalah turunan kelas Kendaraaan

```Python
class Kendaraan:
    def berjalan(self):
        print('berjalan)

class Mobil(kendaraan):
    pass
```
kemudian ketika kita buat objek dan memanggil fungsi berjalan
```Python
sepeda = Kendaraan()
berjalan()
```