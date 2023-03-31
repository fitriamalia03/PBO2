# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang berjalan.")
class Mobil(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Mobil ini sedang belok.")

motorA = Mobil("Mobil", "Sedan", "Hitam", 150)
motorA.berkendara() 
motorA.belok() 