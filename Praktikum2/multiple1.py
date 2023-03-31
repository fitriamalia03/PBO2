# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Customer:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def membeli(self):
        print(self.nama, "sedang membeli paket di aplikasi Hijau ")
    
class Kurir:
    def __init__(self, nama, nim, kurir):
        self.nama = nama
        self.nim = nim
        self.kurir = kurir
    def mengantar(self):
        print(self.nama, "sedang mengantar paket ke kurir", self.kurir)

class CustomerKurir(Customer, Kurir):
    def __init__(self, nama, nim, kurir):
        Customer.__init__(self, nama, nim)
        Kurir.__init__(self, nama, nim, kurir)
    def membayar(self):
        print(self.nama,"dengan NIM", self.nim, "sedang membayar paket ke kurir", self.kurir)
mhs_kurir = CustomerKurir("Fitri Amalia Nurfathir", "210511005", "JNE")
mhs_kurir.membeli() 
mhs_kurir.mengantar() 
mhs_kurir.membayar() 