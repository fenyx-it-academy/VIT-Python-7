#1.Sorunun Cevabı
#--------------------
 dosya=input('Lütfen dosya adı giriniz:  ')   #Kullanıcıdan dosya adı istiyoruz
 file=open(dosya,"r")    #dosyayı okuma modunda açıyorz
 toplam=0
 satir_sayisi=0
 for satir in file:
     satir_sayisi+=1    #her döngüde satır sayısını 1 artırıyoruz
     toplam+=int(satir)  #toplam sayısına her döngüde bir sonraki satırın sayılarını ekliyoruz
 ort=toplam/satir_sayisi   #ortalama hesaplamak için toplamı satır sayısına bölüyoruz
 print('sayıların toplamı:',toplam)  #ekrana yazdırma işlemleri
 print('sayıların ortalaması',ort)
 file.close()  # dosyayı kapatıyoruz

#2.sorunun Cevabı
#---------------------------
dosya=input('Lütfen dosya adı giriniz:  ')   #Kullanıcıdan dosya adı istiyoruz
file=open(dosya,"r")    #dosyayı okuma modunda açıyorz
satir_no=1     #satır no için değişken tanımlıyoruz
metin=""       #satır no ekleneerek oluşturulacak yeni metin için bos değişken tanımlıyoruz
for satir in file:   #her satırı okuyoruz 
    metin+=str(satir_no)+"-"+satir   #her satırın başına satır no ekleyip metin dosyasına aktarıyoıruz
    satir_no+=1      #her seferinde satır numarasını bir artırıyoruz
file.close()     #dosyayı kapatıp bu sefer yazma modunda tekrar açıyoruz
file=open(dosya,"w")
file.write(metin)   #az önce for döngüsü ile oluşturduğumuz metin dosyasını diğer dosyanın üzerine yazıyoruz
print('Dosya Güncellendi')   #işlem sonucunu ekrana yazdırıp dosyayı kapatıyoruz.
file.close()

#3.sorunun Cevabı
#---------------------------
import json
        
giris=input('Öğrenci Listesi İçin-----1\nYeni ÖğrenciEklemek İçin--2\n')
if giris =="1":
    with open("students.json") as file:
        veriler=json.load(file)
        print(veriler)

elif giris=="2":
    
    ad=input("İsim Giriniz:  ")
    soyad=input("Soyisim Giriniz:  ")
    yas=input("Yaş Giriniz:   ")
    yeni_ogrenci={'ad':ad,'soyad':soyad,'yas':yas}
    
    with open("students.json", "a",encoding="utf8") as file:
        json.dump(yeni_ogrenci,file)
        
