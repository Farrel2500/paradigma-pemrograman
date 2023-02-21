def input_alas_Dan_tinggi():
    alas=float(input("Masukan alas: "))
    tinggi=float(input("Masukan alas: "))

    return alas, tinggi

def hitung_luas(alas,tinggi):
    return 0.5 * alas * tinggi

print(hitung_luas(5,10))

alas,tinggi = input_alas_Dan_tinggi()
print(hitung_luas(alas, tinggi))