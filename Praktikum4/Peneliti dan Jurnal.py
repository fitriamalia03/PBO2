# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Peneliti:
    def __init__(self, name):
        self.name = name
        self.judul = Judul()
        print("Karya Fitri Amalia Nurfathir")

class Jurnal:
    def __init__(self, name):
        self.name = name

class Judul:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print ("Judul Jurnal: ", item.name)

    def remove_item(self, item):
        self.items.remove(item)

peneliti = Peneliti(" ")
jurnal1 = Jurnal("Analisa Dan Perancangan Sistem Informasi Akademik Berbasis Web Pada SMAN 1 Arjawinangun")
jurnal2 = Jurnal("Rancang Bangun Aplikasi Persediaan Pupuk Bersubsidi")

print("="*40)
peneliti.judul.add_item(jurnal1)
peneliti.judul.add_item(jurnal2)
peneliti.judul.items
print(" ")
