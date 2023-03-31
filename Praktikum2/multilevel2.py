# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Buah:
    def __init__(self, name):
        self.name = name
    def Rasa(self):
        print("Buah-buahan memiliki banyak manfaat")

class Jeruk(Buah):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa
    def Rasa(self):
        print("Jeruk mengandung vitamin C")

class JerukMandarin(Jeruk):
    def __init__(self, name, rasa, asal):
        super().__init__(name, rasa)
        self.asal = asal
    def Rasa(self):
        print("Jeruk Mandarin memiliki rasa yang manis")

JerukMandarinA = JerukMandarin("Jeruk Mandarin"," manis", "Asia Selatan")
JerukB = Jeruk("Lemon", "Asam")
buahC = Buah("Buah apa yang enak?")
JerukMandarinA.Rasa()
JerukB.Rasa()
buahC.Rasa()