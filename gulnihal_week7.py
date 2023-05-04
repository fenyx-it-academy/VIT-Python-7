#soru1

dosya_adi = input("Dosya adini girin: ")

with open(dosya_adi, "r") as dosya:
    toplam = 0
    satir_sayisi = 0
    for satir in dosya:
        sayilar = satir.split()
        for sayi in sayilar:
            toplam += float(sayi)
        satir_sayisi += 1

ortalama = toplam / satir_sayisi

print("Toplam:", toplam)
print("Ortalama:", ortalama)

#soru2


#soru3
#ilk olarak bir json dosyasi olusturuyoruz.
import json

ogrenciler = [
    {"ad": "Sevgi", "soyad": "Guney", "yas": 20},
    {"ad": "Yunus", "soyad": "Yildirim", "yas": 28},
    {"ad": "Gulnihal", "soyad": "Ozkan", "yas": 24}
]

with open("students.json", "w") as dosya:
    json.dump(ogrenciler, dosya)
    
#################

import json

with open("students.json", "r") as dosya:
    ogrenciler = json.load(dosya)

while True:
    print("1- Yeni ogrenci ekle")
    print("2- Ogrenci listesini goruntule")
    print("3- Cikis yap")
    secim = input("Seciminizi girin (1-3): ")

    if secim == "1":
        ad = input("Ogrenci adini girin: ")
        soyad = input("Ogrenci soyadini girin: ")
        yas = input("Ogrenci yasini girin: ")
        ogrenci = {"ad": ad, "soyad": soyad, "yas": yas}
        ogrenciler.append(ogrenci)
        with open("students.json", "w") as dosya:
            json.dump(ogrenciler, dosya)
        print("Öğrenci eklendi.")
    elif secim == "2":
        for i, ogrenci in enumerate(ogrenciler):
            print(f"{i+1}- {ogrenci['ad']} {ogrenci['soyad']}, {ogrenci['yas']} yaşında")
    elif secim == "3":
        print("Program sonlandirildi.")
        break
    else:
        print("Gecersiz secim. Lütfen tekrar deneyin.")
    
    
    
    
