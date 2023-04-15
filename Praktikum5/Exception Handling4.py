dictionary = {"lima": 5, "sepuluh": 10, "seratus": 100}

try:
    value = dictionary["lima puluh"]
except KeyError:
    print("Key yang diminta tidak ditemukan, Coba masukan kembali dengan key yang berbeda!")
