# NIM    : 210511005
# Nama   : Fitri Amalia Nurfathir
# Kelas  : TIF21A (R1)

class SuhuKelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin
        
    def to_celcius(self):
        return (self.kelvin - 273) 
    
    def to_fahrenheit(self):
        return 9/5 * (self.kelvin - 273) + 32
    
    def to_reamur(self):
        return 4/5 * (self.kelvin - 273)
    
suhu = SuhuKelvin(36)
celcius = suhu.to_celcius()
fahrenheit = suhu.to_fahrenheit()
reamur = suhu.to_reamur()

print(f"Konversi {suhu.kelvin} derajat Kelvin adalah {celcius} derajat Celcius")
print(f"Konversi {suhu.kelvin} derajat Kelvin adalah {fahrenheit} derajat Fahrenheit")
print(f"Konversi {suhu.kelvin} derajat Kelvin adalah {reamur} derajat Reamur")