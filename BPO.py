class Segitiga:
    def __init__(self,alas,tinggi):
        self.alas= alas
        self.tinggi= tinggi

    def get_luas(self):
        return 0.5 + self.alas * self.tinggi
Segitiga1 = Segitiga(5,10)
Segitiga2 = Segitiga(3,9)
Segitiga3 = Segitiga(5,10)
print ('Luas segitiga1 : ', Segitiga1.get_luas())
print ('Luas segitiga1 : ', Segitiga2.get_luas())
print ('Luas segitiga1 : ', Segitiga3.get_luas())
