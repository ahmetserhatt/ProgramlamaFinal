from Calisan import calisan

class mavi_yaka(calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,  sektor, tecrube, maas, yipranma_payi ):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk,  sektor, tecrube, maas)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.__tecrube >= 2:
                if self.__maas == 15000:
                    return (self.__maas % self.__tecrube) / 2 + (self.__yipranma_payi * 10)
                elif self.__maas < 15000:
                    return (self.__maas % self.__tecrube) / 2 + (self.__yipranma_payi * 10)
                elif self.__maas < 25000:
                    return (self.__maas % self.__tecrube) / 3 + (self.__yipranma_payi * 10)
            return 0
        except ZeroDivisionError:
            print("Tecrube sıfır olamaz!")
        except Exception as e:
            print("Bir hata oluştu:", e)



    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrube: {self.get_tecrube()} ay, Yeni Maas: {self.zam_hakki()}"
