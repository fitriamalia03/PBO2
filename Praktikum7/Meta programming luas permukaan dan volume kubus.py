# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class KubusMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

        def luaspermukaan(cls, sisi):
            return 6 * sisi * sisi
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, sisi):
            return sisi * sisi * sisi
        cls.volume = classmethod(volume)

class Luaspermukaandanvolume(metaclass=KubusMeta):
    pass

A = Luaspermukaandanvolume()
B = A.luaspermukaan(5)
C = A.volume(5)
print('Luas Permukaan Kubus:',B)
print('Volume Kubus:',C)