# NIM    : 210511005
# Nama   : Fitri Amalia Nurfathir
# Kelas  : TIF21A (R1)

class SuhuReamur:
    def __init__(self, reamur):
        self.reamur = reamur
    
    def to_celcius(self):
        return (5/4 * self.reamur)
    
    def to_fahrenheit(self):
        return (9/4 * self.reamur) + 32
    
    def to_kelvin(self):
        return (5/4 * self.reamur) + 273

suhu = SuhuReamur(36)
celcius = suhu.to_celcius()
fahrenheit = suhu.to_fahrenheit()
kelvin = suhu.to_kelvin()

print(f"Konversi {suhu.reamur} derajat Reamur adalah {celcius} derajat Celcius")
print(f"Konversi {suhu.reamur} derajat Reamur adalah {fahrenheit} derajat Fahrenheit")
print(f"Konversi {suhu.reamur} derajat Reamur adalah {kelvin} derajat Kelvin")