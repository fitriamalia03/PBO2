class Buku:
    def __init__(self, judul, penulis, Tahun):
     self.judul = judul
     self.penulis = penulis
     self.Tahun = Tahun
    def info(self):
     print(f"Judul: {self.judul}\nPenulis: {self.penulis}\nTahun:{self.Tahun}")
bukuA = Buku("Percy Jackson and the Last Olympian", "Rick Riordan", "2009")
bukuA.info()