#Metin Dosyasi Islemleri
def dosya_okuma():
    dosya_adi = input("Dosyanizin adini yazin:")
    toplam = 0
    with open(dosya_adi,"r") as d:
        liste = d.readlines()
        for x in liste:
            toplam += int(x)
            ortalama = toplam / len(liste)
    print("Ortalama deger:",ortalama)

dosya_okuma()

#Dosya Duzenleme
dosya = input("Dosya adi:")
satir = 1
with open(dosya,"r+") as d:
    liste = d.readlines()
    d.seek(0)
    for x in liste:
        sira = (str(satir),"-",x)
        satir += 1
        d.writelines(sira)
print(dosya)

#Json islemleri
import json


with open("/Users/ahmetmesutcelem/VIT/Odevler/students.json") as dosya:
    ogrenciler = json.load(dosya)
    bilgi = ogrenciler["ogrenciler"]
    # print(bilgi)


while True:
    secim = input("""
    1-> Yeni ogrenci ekle
    2-> Ogrenci bilgileri
    3-> Cikis

    BIR SECIM YAPIN:
    """)
    if secim == "3":
        break
    elif secim == "1":
        ad = input("Ogrencinin Adi:")
        soyad = input("Ogrencinin soyadi:")
        yas = input("Ogrencinin yasi:")
        ogrenci = {"Ad":ad,"Soyad":soyad,"Yas":yas}
        bilgi.append(ogrenci)
        with open("/Users/ahmetmesutcelem/VIT/Odevler/students.json","w") as ekle:
            json.dump(bilgi,ekle,indent=4)
    elif secim == "2":
        ara = input("Ogrenci Adi:")
        for x in bilgi:
            if ara == x["Ad"]:
                print("Ogrencinin adi:",x["Ad"])
                print("Ogrencinin adi:",x["Soyad"])
                print("Ogrencinin adi:",x["Yas"])
    else:
        print("Hatali Giris! Tekrar deneyin!")
