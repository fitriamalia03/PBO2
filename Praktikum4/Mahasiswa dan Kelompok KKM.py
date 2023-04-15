# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Mahasiswa:
    def __init__(self, name):
        self.name = name
        self.anggota = Anggota()
        print("Daftar Nama Mahasiswa Kelompok KKM")

class Kelompok_KKM:
    def __init__(self, name):
        self.name = name

class Anggota:
    def __init__(self):
        self.items = []
    
    def add_item1(self, item):
        self.items.append(item)
        print("Kelompok 1: ", item.name)
    def add_item2(self, item):
        print("Kelompok 2: ", item.name)
    
    def remove_item(self, item):
        self.items.remove(item)

mahasiswa = Mahasiswa(" ")
kel1 = Kelompok_KKM("Arhan, Shanbin, Gian")
kel2 = Kelompok_KKM("Karina, Giselle, Aby")

print("="*40)
mahasiswa.anggota.add_item1(kel1)
mahasiswa.anggota.add_item2(kel2)
mahasiswa.anggota.items
print(" ")
