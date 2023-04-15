list_angka = [20, 30, 40, 50]

try:
    value = list_angka[51]
except IndexError:
    print("Index yang diminta tidak ada!")
