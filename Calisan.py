from Insan import insan

class calisan(insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,  sektor, tecrube, maas ):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.__kontrol_sektor(sektor) #burayı anlamadım neden sektor değil
        self.__tecrube = int(tecrube)
        self.__maas = maas

    def __kontrol_sektor(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor in sektorler:
            return sektor
        else:
            raise ValueError("Geçersiz sektor!")

    def get_sektor(self):
        return self.__sektor

    def get_tecrube(self):
        return self.__tecrube

    def get_maas(self):
        return self.__maas

    def set_sektor(self, sektor):
        self.__sektor = self.__kontrol_sektor(sektor)

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        try:
            tecrube = int(self.__tecrube)
            maas = int(self.__maas)
        except ValueError:
            print("Tecrube ve maas sayısal olmalı!")
            return

        if tecrube < 0:
            print("Tecrube sıfırdan büyük olmalı!")
            return

        if tecrube < 2:
            return 0
        elif 2 <= tecrube < 4 and maas < 15000:
            return maas * tecrube / 100
        elif tecrube >= 4 and maas < 25000:
            return (maas * tecrube) / 200
        else:
            return 0



def __str__(self):
    return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {self.zam_hakki()}"



