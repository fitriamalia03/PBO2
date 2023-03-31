# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis
    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")
class Mamalia(Hewan):
    def __init__(self, nama):
        self.nama = nama
    def display_info(self):
        super().display_info()
        print(f"Nama hewan: {self.nama}")
class Herbivora(Hewan):
    def __init__(self, jenis, makanan):
        super().__init__(jenis)
        self.makanan = makanan
    def display_info(self):
        super().display_info()
        print(f"Jenis makanan: {self.makanan}")
class Kangguru(Mamalia, Herbivora):
    def __init__(self, jenis, nama, makanan):
        Mamalia.__init__(self, nama)
        Herbivora.__init__(self, jenis, makanan)
    def display_info(self):
        super().display_info()
        print(f"Jenis hewan: {self.jenis}")
# contoh penggunaan
kangguruA = Kangguru("Mamalia", "Kangguru", "Rerumputan")
kangguruA.display_info()