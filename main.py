import pandas as pd
from Insan import insan
from Issiz import issiz
from Calisan import calisan
from MaviYaka import mavi_yaka
from BeyazYaka import beyaz_yaka

#insan nesneleri
insan1 = insan("12345678901", "Ali", "Yılmaz", 25, "Erkek", "Türk")
insan2 = insan("98765432109", "Ayşe", "Kaya", 30, "Kadın", "Türk")

print("İnsan 1 Bilgileri:")
print(insan1)

print("\nİnsan 2 Bilgileri:")
print(insan2)

print("\n-------------------------------------------------------------------\n")

# issiz nesneleri
statu_dict1={"Mavi yaka":3,"Beyaz yaka":5,"Yönetici":2}
statu_dict2={"Mavi yaka":20,"Beyaz yaka":5,"Yönetici":2}
statu_dict3={"Mavi yaka":1,"Beyaz yaka":2,"Yönetici":3}

issiz1 = issiz("12345678901", "Ali", "Yılmaz", 25, "Erkek", "Türk", statu_dict1)
issiz2 = issiz("98765432109", "Ayşe", "Kaya", 30, "Kadın", "Türk", statu_dict2)
issiz3 = issiz("45678901234", "Mehmet", "Demir", 35, "Erkek", "Türk", statu_dict3)

print("İşsiz 1 Bilgileri:")
print(issiz1)

print("\nİşsiz 2 Bilgileri:")
print(issiz2)

print("\nİşsiz 3 Bilgileri:")
print(issiz3)

print("\n-------------------------------------------------------------------\n")

# CALİSAN NESNELERİ
calisan1 = calisan("12345678901", "Ali", "Yılmaz", 2, "Erkek", "Türk", "teknoloji", 6, 12000)
calisan2 = calisan("98765432109", "Ayşe", "Kaya", 3, "Kadın", "Türk", "muhasebe", 3, 18000)
calisan3 = calisan("45678901234", "Mehmet", "Demir", 5, "Erkek", "Türk", "inşaat", 8, 25000)

print("Çalışan 1 Bilgileri:")
print(calisan1)

print("\nÇalışan 2 Bilgileri:")
print(calisan2)

print("\nÇalışan 3 Bilgileri:")
print(calisan3)

print("\n-------------------------------------------------------------------\n")

# MAVİ YAKA NESNELERİ
mavi_yaka1 = mavi_yaka("12345678901", "Ali", "Yılmaz", 2, "Erkek", "Türk", "teknoloji", 6, 12000, 1000)
mavi_yaka2 = mavi_yaka("98765432109", "Ayşe", "Kaya", 3, "Kadın", "Türk", "muhasebe", 3, 18000, 1500)
mavi_yaka3 = mavi_yaka("45678901234", "Mehmet", "Demir", 5, "Erkek", "Türk", "inşaat", 8, 25000, 2000)

print("Mavi Yaka 1 Bilgileri:")
print(mavi_yaka1)

print("\nMavi Yaka 2 Bilgileri:")
print(mavi_yaka2)

print("\nMavi Yaka 3 Bilgileri:")
print(mavi_yaka3)

print("\n-------------------------------------------------------------------\n")

#BEYAZ YAKA NESNELERİ
beyaz_yaka1 = beyaz_yaka("12345678901", "Ali", "Yılmaz", 2, "Erkek", "Türk", "teknoloji", 6, 12000, 1000)
beyaz_yaka2 = beyaz_yaka("98765432109", "Ayşe", "Kaya", 3, "Kadın", "Türk", "muhasebe", 3, 18000, 1500)
beyaz_yaka3 = beyaz_yaka("45678901234", "Mehmet", "Demir", 5, "Erkek", "Türk", "inşaat", 8, 25000, 2000)

print("Beyaz Yaka 1 Bilgileri:")
print(beyaz_yaka1)

print("\nBeyaz Yaka 2 Bilgileri:")
print(beyaz_yaka2)

print("\nBeyaz Yaka 3 Bilgileri:")
print(beyaz_yaka3)

# DataFrame oluşturma
data = pd.DataFrame({
                "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan"],
                "T.C. Kimlik No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no()],
                "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad()],
                "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad()],
                "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas()],
                "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet()],
                "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk()],
                "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor()],
                "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube()],
                "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas()],
                "Yeni Maaş": [calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki()]
        })

print(data)

data.fillna(0, inplace=True)
grouped = data.groupby("Nesne Değeri").agg({"Tecrübe": "mean", "Maaş": "mean"})


print(grouped)
maas_ustunde = data[data["Maaş"] > 15000]
sayi = len(maas_ustunde)
print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", sayi)
sorted_data = data.sort_values("Maaş")
print(sorted_data)
tecrube_ustunde = data[(data["Nesne Değeri"] == "Beyaz Yaka") & (data["Tecrübe"] > 3)]

print(tecrube_ustunde)
yuksek_maas = data[data["Maaş"] > 10000].iloc[2:5, [1, 10]]

print(yuksek_maas)
yeni_dataframe = data[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]

print(yeni_dataframe)
