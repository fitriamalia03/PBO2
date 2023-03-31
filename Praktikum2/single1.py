# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "bergerak")
class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Meow!")
        
kucingA = Kucing("Louis", 2, "Siam")
kucingA.bergerak() 
kucingA.bersuara() 