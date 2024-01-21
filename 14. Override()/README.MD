## Apa Itu Overriding?
 **Overriding** adalah sebuah fitur dalam konsep object oriented programming (OOP) untuk melakukan penimpaan dari fungsi yang telah didefinisikan sebelumnya

## Cara Melakukan Overriding

Misal kita mempunyai dua kelas, yaitu kelas Kendaraan dan kelas Mobil yang mana :
- **Kelas Kendaraan** adalah kelas induk
- **Kelas Mobil** adalah turunan kelas Kendaraaan

```python
class Kendaraan:
    def berjalan(self):
        print('berjalan...')

class Mobil(Kendaraan):
    pass

# membuat objek
sepeda = Kendaraan()
sedan = Mobil()

# memanggil method/function berjalan()
sepeda.berjalan()
sedan.berjalan()
```
Output :
```python
berjalan...
berjalan...
```

Melakukan overriding
```python
class Kendaraan:
    def berjalan(self):
        print('berjalan...')

class Mobil(Kendaraan):
    def berjalan(self):
        print('berjalan dengan cepat...')
    
# membuat objek
sepeda = Kendaraan()
sedan = Mobil()

# memanggil method/function berjalan()
sepeda.berjalan()
sedan.berjalan()
```
Output :
```python
berjalan...
berjalan dengan cepat...
```

## Kesimpulan
 Dengan melakukan overriding kita dapat menimpa *method* yang sebelumnya telah dibuat di kelas induk, sehingga tidak perlu khawatir program akan bingung memilih *method* yang mana karena yang digunakan adalah *method* pada kelas turunan bukan di kelas induk
