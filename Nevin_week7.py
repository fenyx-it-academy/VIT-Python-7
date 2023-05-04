cevap1
#Bir metin dosyasında satır satır saklanan sayıların toplamını ve 
# ortalamasını hesaplayan bir program yazın. Programınız aşağıdaki işlemleri gerçekleştirmelidir:
#Kullanıcıdan dosya adı isteyin.
#Dosyayı okuyun ve satırlardaki sayıları toplayın.
#Toplam ve satır sayısını kullanarak ortalama değeri hesaplayın.
#Sonuçları ekrana yazdırın.
filename = input('dosya adini giriniz:')
try:
    file= open(filename, 'r') 
except FileNotFoundError:
    print("Dosya bulunamadı.")
else:
      toplam=0
      satir=0
      
      for i in file:
            try:
             sayi=float(i)
            except ValueError:
                  print("Gecersiz sayi"+ i)
            else:
                  toplam+=int(sayi)
                  satir+=1
  
file.close()
if satir>1:
      ortalama=toplam/satir
      print(f'Toplam: {toplam} ,  Ortalama:{ortalama}')
else:
      print('Dosyada sayi yok')
    
Cevap2
# Bir metin dosyasındaki her satırın başına satır numarası ekleyen bir program yazın. 
# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve her satırın başına satır numarası ekleyin.
# Dosyayı güncellenmiş içerikle tekrar yazın.
filename = input('Dosyanin Adini Giriniz:')
with open(filename, 'r')as file:
    liste=file.readlines()
with open(filename, 'w') as file:
    nieuwlist=list(enumerate(liste,1))
    print(nieuwlist)
    for i ,line in nieuwlist:
        file.write(f'{i}.{line}')
Cevap3
import json

students = [
    {"ad": "Semra", "soyad": "Koca", "yas": 22},
    {"ad": "Yahya", "soyad": "Yalin", "yas": 28},
    {"ad": "Gulsum", "soyad": "Kaya", "yas": 27}
]

with open("students.json", "w") as file:
    json.dump(students, file)
    

 # students.json adlı bir JSON dosyasında öğrenci bilgilerini saklayın. Bu dosya, ad, soyad ve yaş bilgilerini içeren öğrenci nesnelerinden oluşan bir liste içermelidir. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# students.json dosyasını okuyun.
# Kullanıcıdan yeni bir öğrenci ekleme veya mevcut öğrencilerin listesini görüntüleme seçeneklerini sunun.
# Yeni öğrenci ekleme seçeneği seçilirse, kullanıcıdan öğrenci adı, soyadı ve yaşını isteyin ve JSON dosyasına ekleyin.
# Öğrenci listesini görüntüleme seçeneği seçilirse, öğrenci bilgilerini ekrana yazdırın.
# JSON dosyasını güncelleyin ve programı sonlandırın
import json

with open("students.json","r") as file:
    students=json.load(file)
    
while True:
    print("1-Ogrenci ekleme\n"+"2-Ogrenci listesi\n"+"3-Cikis")
    secim=int(input("seciminizi giriniz:"))
    if secim==1:
        ad=input('Ogrenci adini giriniz:')
        soyad=input('Ogrenci soyad giriniz:')
        yas=input('Ogrenci yas :')
        new_student={"ad":ad, "soyad":soyad,"yas":yas}
        students.append(new_student)
        with open("students.json", "w") as file:
            json.dump(students, file)
            print('Ogrenci Basariyla Eklendi')
    elif secim==2:
            print('Ogrenci Listesi Goruntuleniyor')
            for i, ogrenci in enumerate(students):
                 print(f"{i+1}- {ogrenci['ad']} {ogrenci['soyad']}, {ogrenci['yas']} yaşında")
    elif secim==3:
        break
    else:
        print('Gecersiz  Secim Lutfen Tekrar Deneyin')
       
    

      
