# # VIT-Python-7
#Soru 1 
# ## Metin Dosyası İşlemleri
# Bir metin dosyasında satır satır saklanan sayıların toplamını ve ortalamasını hesaplayan bir program yazın. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# * Kullanıcıdan dosya adı isteyin.
# * Dosyayı okuyun ve satırlardaki sayıları toplayın.
# * Toplam ve satır sayısını kullanarak ortalama değeri hesaplayın.
# * Sonuçları ekrana yazdırın.

#Cevap 1
# * Kullanıcıdan dosya adı iste.
dosya_adi = input("Dosya adını girin: ")

# Toplam ve satır sayısını sıfıra ayarla
toplam = 0
satir_sayisi = 0

# Dosyayı aç ve oku
with open(dosya_adi, 'r') as dosya:
    # Dosyanın her satırını oku
    for satir in dosya:
        # Satırı bir tam sayıya dönüştür
        try:
            sayi = int(satir.strip())
        except ValueError:
            # Satır bir sayı değilse, devam et
            continue
        
        # Toplamı ve satır sayısını güncelle
        toplam += sayi
        satir_sayisi += 1

# Ortalamayı hesapla
if satir_sayisi > 0:
    ortalama = toplam / satir_sayisi
else:
    ortalama = 0

# Sonuçları ekrana yazdır
print("Toplam: ", toplam)
print("Ortalama: ", ortalama)





#Soru 2 
# ## Dosya Düzenleme
# Bir metin dosyasındaki her satırın başına satır numarası ekleyen bir program yazın. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# * Kullanıcıdan dosya adı isteyin.
# * Dosyayı okuyun ve her satırın başına satır numarası ekleyin.
# * Dosyayı güncellenmiş içerikle tekrar yazın.



#Cevap 2
dosya_adi = input("Dosya adını girin: ")

# Dosyayı aç ve oku
with open(dosya_adi, 'r') as dosya:
    satirlar = dosya.readlines()

# Satırların sayısını hesapla
satir_sayisi = len(satirlar)

# Dosyayı tekrar yazmak için aç
with open(dosya_adi, 'w') as dosya:
    # Her satıra satır numarası ekle ve dosyaya yaz
    for i in range(satir_sayisi):
        satir = satirlar[i].strip()
        satir_numarasi = str(i+1)
        satir = satir_numarasi + ". " + satir + "\n"
        dosya.write(satir)

# İşlem tamamlandı mesajı yazdır
print("Dosya güncellendi.")



#Soru 3
# ## JSON İşlemleri
# students.json adlı bir JSON dosyasında öğrenci bilgilerini saklayın. Bu dosya, ad, soyad ve yaş bilgilerini içeren öğrenci nesnelerinden oluşan bir liste içermelidir. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# * students.json dosyasını okuyun.
# * Kullanıcıdan yeni bir öğrenci ekleme veya mevcut öğrencilerin listesini görüntüleme seçeneklerini sunun.
# * Yeni öğrenci ekleme seçeneği seçilirse, kullanıcıdan öğrenci adı, soyadı ve yaşını isteyin ve JSON dosyasına ekleyin.
# * Öğrenci listesini görüntüleme seçeneği seçilirse, öğrenci bilgilerini ekrana yazdırın.
# # * JSON dosyasını güncelleyin ve programı sonlandırın.


#Cevap 3


import json

dosya_adi = "students.json"

# Dosyayı oku
with open(dosya_adi, 'r') as dosya:
    ogrenciler = json.load(dosya)

# Seçenekleri görüntüle ve kullanıcıdan seçim yapmasını iste
while True:
    print("1. Yeni öğrenci ekle")
    print("2. Öğrenci listesini görüntüle")
    print("3. Çıkış yap")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        # Kullanıcıdan yeni öğrenci bilgilerini al
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        yas = input("Öğrenci yaş: ")

        # Yeni öğrenci nesnesini oluştur
        yeni_ogrenci = {
            "ad": ad,
            "soyad": soyad,
            "yas": yas
        }

        # Öğrenci listesine ekle
        ogrenciler.append(yeni_ogrenci)

    elif secim == "2":
        # Öğrenci listesini ekrana yazdır
        for i, ogrenci in enumerate(ogrenciler, start=1):
            print(f"{i}. {ogrenci['ad']} {ogrenci['soyad']} ({ogrenci['yas']})")

    elif secim == "3":
        # JSON dosyasına güncellenmiş öğrenci listesini yaz
        with open(dosya_adi, 'w') as dosya:
            json.dump(ogrenciler, dosya)
        # Programı sonlandır
        break

    else:
        # Geçersiz seçim yapıldı uyarısı ver
        print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")
