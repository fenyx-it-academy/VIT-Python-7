#cevap1
dosya_adi = input("Dosya adını girin: ")

with open(dosya_adi, "r") as dosya:
    satirlar = dosya.readlines()
    toplam = 0
    satir_sayisi = 0
    for satir in satirlar:
        sayi = int(satir)
        toplam += sayi
        satir_sayisi += 1

    ortalama = toplam / satir_sayisi
    print("Sayıların toplamı:", toplam)
    print("Sayıların ortalamasi:", ortalama)


#cevap2
dosya_adi = input("Dosya adını girin: ")

with open(dosya_adi, "r+") as dosya:
    satirlar = dosya.readlines()
 
    for i, satir in enumerate(satirlar, 1):
        dosya.write(f"{i}. {satir}\n")

print("Dosya güncellendi.")

#cevap3

import json

with open(r"C:\Users\YasinSohret\Desktop\DENEMELER\students.json", "r") as f:
    students = json.load(f)
while True:
    choice = input("\nÖğrenci eklemek için '1', öğrenci listesini görüntülemek için '2' yazın (çıkış yapmak için 'q'): ")
    if choice == "1":
        ad = input("Ogrenci adini girin: ")
        soyad = input("Ogrenci soyadini girin: ")
        yas = input("Ogrenci yasini girin: ")
        student = {"ad": ad, "soyad": soyad, "yas": yas}
        students.append(student)
        with open("students.json", "w") as dosya:
            json.dump(students, dosya)
        print(f"{ad} {soyad} adlı öğrenci basariyla eklendi.") 
    elif choice == "2":
        for i, student in enumerate(students):
            print(f"{i+1}- {student['ad']} {student['soyad']}, {student['yas']} yaşında")
    elif choice == "3":
        print("Program sonlandirildi.")
        break
    else:
        print("Gecersiz secim. Lütfen tekrar deneyin.")




