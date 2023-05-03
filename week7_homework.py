# Metin Dosyası İşlemleri
# Bir metin dosyasında satır satır saklanan sayıların toplamını ve ortalamasını hesaplayan bir program yazın. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve satırlardaki sayıları toplayın.
# Toplam ve satır sayısını kullanarak ortalama değeri hesaplayın.
# Sonuçları ekrana yazdırın.
toplam = 0
filename = input("Dosya adınız giriniz :")
with open("week7/"+filename+".txt") as dosya:
    veri = dosya.readlines()
    for i in veri:
        toplam += int(i)
    print(f"Toplam satir sayisi: {len(veri)}\nSayilarin toplami: {toplam}\nOrtalama: {(toplam/len(veri)):.2f}")

# ------------------------------------------------------------

# Dosya Düzenleme
# Bir metin dosyasındaki her satırın başına satır numarası ekleyen bir program yazın. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve her satırın başına satır numarası ekleyin.
# Dosyayı güncellenmiş içerikle tekrar yazın.

with open("week7/metin.txt", "r") as dosya:

        words = dosya.read().split()
        print(words)

number = 1
with open("week7/metin.txt", "w") as dosya:

        for i in words:
                dosya.writelines(str(number)+"-"+i+"\n")
                number += 1

with open("week7/metin.txt", "r") as dosya:
        print(dosya.read())

#------------------------------------------------------------

# JSON İşlemleri
# students.json adlı bir JSON dosyasında öğrenci bilgilerini saklayın. Bu dosya, ad, soyad ve yaş bilgilerini içeren öğrenci nesnelerinden oluşan bir liste içermelidir. Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# students.json dosyasını okuyun.
# Kullanıcıdan yeni bir öğrenci ekleme veya mevcut öğrencilerin listesini görüntüleme seçeneklerini sunun.
# Yeni öğrenci ekleme seçeneği seçilirse, kullanıcıdan öğrenci adı, soyadı ve yaşını isteyin ve JSON dosyasına ekleyin.
# Öğrenci listesini görüntüleme seçeneği seçilirse, öğrenci bilgilerini ekrana yazdırın.
# JSON dosyasını güncelleyin ve programı sonlandırın.

import json

with open("week7/students.json","r") as file:

        file_data = json.load(file)
        
while True:
        sorgu = str(input("""
        
        1 --- Add students
        2 --- Show students 

        """))

        if sorgu == "1":

                name = input("Enter new name:")
                surname = input("Enter new surname:")
                age = str(input("Enter new age :"))
                
                with open("week7/students.json","w") as file:

                        a = {"name":name, "surname":surname,"age":age}
                        file_data["students"].append(a)
                        json.dump(file_data,file,indent = 4,ensure_ascii=False)
                        break

        elif sorgu == "2":

                with open("week7/students.json","r") as file:

                        print(file.read())
                        break

#students.json
{
    "students": [
        {
            "name": "cafer",
            "surname": "erdem",
            "age": "27"
        },
        {
            "name": "a",
            "surname": "b",
            "age": "1"
        }
    ]
}
