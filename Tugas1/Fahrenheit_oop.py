# NIM    : 210511005
# Nama   : Fitri Amalia Nurfathir
# Kelas  : TIF21A (R1)

class SuhuFahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def to_celcius(self):
        return (5/9) * self.fahrenheit - 32
    
    def to_kelvin(self):
        return (5/9) * (self.fahrenheit - 32) + 273
    
    def to_reamur(self):
        return (4/9) * self.fahrenheit - 32

suhu = SuhuFahrenheit(36)
celcius = suhu.to_celcius()
kelvin = suhu.to_kelvin()
reamur = suhu.to_reamur()

print(f"Konversi {suhu.fahrenheit} derajat Fahrenheit adalah {celcius} derajat Reamur")
print(f"Konversi {suhu.fahrenheit} derajat Fahrenheit adalah {kelvin} derajat Kelvin")
print(f"Konversi {suhu.fahrenheit} derajat Fahrenheit adalah {reamur} derajat Fahrenheit")