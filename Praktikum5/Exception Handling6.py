class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

kucing = Kucing("Louis", 20)

try:
    print(kucing.asal)
except AttributeError:
    print("Objek yang anda minta tidak ditemukan!")
