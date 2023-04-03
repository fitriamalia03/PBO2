
# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

from playsound import *


class Animal:
    def make_sound(self):
        print("Animal Sound")
print("="*40)

class Anjing(Animal):
    def make_sound(self):
        print('Anjing')
        playsound('anjing.mp3')

class Ayam(Animal):
    def make_sound(self):
        print('Ayam')
        playsound('ayam.mp3')

class Bebek(Animal):
    def make_sound(self):
        print('Bebek')
        playsound('bebek.mp3')

class Gajah(Animal):
    def make_sound(self):
        print('Gajah')
        playsound('gajah.mp3')

class Kambing(Animal):
    def make_sound(self):
        print('Kambing')
        playsound('kambing.mp3')

class Kucing(Animal):
    def make_sound(self):
        print('Kucing')
        playsound('kucing.mp3')

class Kuda(Animal):
    def make_sound(self):
        print('Kuda')
        playsound('kuda.mp3')

class Sapi(Animal):
    def make_sound(self):
        print('Sapi')
        playsound('sapi.mp3')

class Serigala(Animal):
    def make_sound(self):
        print('Serigala')
        playsound('serigala.mp3')

class Singa(Animal):
    def make_sound(self):
        print('Singa')
        playsound('singa.mp3')

def animal_sound(hewan):
    hewan.make_sound()

hewan = Animal()

anjing = Anjing()
ayam = Ayam()
bebek = Bebek()
gajah = Gajah()
kambing = Kambing()
kucing = Kucing()
kuda = Kuda()
sapi = Sapi()
serigala = Serigala()
singa = Singa()

animal_sound(hewan) 
print("="*40)

# Masukkan nama hewan di bawah ini, Contoh: (serigala)
animal_sound(ayam)

