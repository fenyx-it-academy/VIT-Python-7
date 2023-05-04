# VIT-Python-7
# Metin Dosyası İşlemleri
# Bir metin dosyasında satır satır saklanan sayıların toplamını ve ortalamasını hesaplayan bir program yazın.
# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve satırlardaki sayıları toplayın.
# Toplam ve satır sayısını kullanarak ortalama değeri hesaplayın.
# Sonuçları ekrana yazdırın.

user = input("Dosya adini giriniz: (!!SAYILAR!!) ")

with open("C:\\PYTHON-VIT-DESKTOP\\7.hafta odev\\"+user+".txt", "r") as dosya:
    veri = dosya.readlines()
    toplam=0
    satir_sayisi=0
    for i in veri:
        toplam+=int(i)
        satir_sayisi+=1
    print(f"Toplam satir sayisi: {satir_sayisi}\nSayilarin toplami: {toplam}\nOrtalama: {(toplam/satir_sayisi):.2f}")
    