
# JSON İşlemleri

# students.json adlı bir JSON dosyasında öğrenci bilgilerini saklayın.
# Bu dosya, ad, soyad ve yaş bilgilerini içeren öğrenci nesnelerinden oluşan bir liste içermelidir.
# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# students.json dosyasını okuyun.
# Kullanıcıdan yeni bir öğrenci ekleme veya mevcut öğrencilerin listesini görüntüleme seçeneklerini sunun.
# Yeni öğrenci ekleme seçeneği seçilirse, kullanıcıdan öğrenci adı, soyadı ve yaşını isteyin ve JSON dosyasına ekleyin.
# Öğrenci listesini görüntüleme seçeneği seçilirse, öğrenci bilgilerini ekrana yazdırın.
# JSON dosyasını güncelleyin ve programı sonlandırın.

import json

with open("C:\\PYTHON-VIT-DESKTOP\\7.hafta odev\\student.json","r") as dosya:
    
    dict_dosya=json.load(dosya)
    
    count=len(dict_dosya)
    secim=input("Ogrencileri goruntulemekicin '1'\nOgrenci eklemek icin '2'")
    if secim=="1":
        # print(type(dict_dosya))
        # print(dict(dict_dosya).values())
        print(dict_dosya.values())
    elif secim =="2":
        while True:
            try:
                students_name=input("Ogrencinin adi: ")
                students_surname=input("Ogrencinin soyadi: ")
                students_age=input("Ogrencinin yasi: ")
                if not students_name.isalpha() or not students_surname.isalpha() or not students_age.isdecimal():
                    raise SyntaxError("Hatali giris yaptiniz")
            except SyntaxError as S :
                print(S)
            else:
                count+=1
            
                kayit={"ad":students_name,"soyad":students_surname,"yas":students_age}
                # students.append(kayit)
                dict_dosya[f"student{count}"]=kayit
            with open("C:\\PYTHON-VIT-DESKTOP\\7.hafta odev\\student.json","w") as dosya:
                json.dump(dict_dosya,dosya,indent=4)

                choice = input("Yeni öğrenci kaydı için 'Enter', çıkmak için 'q' tuşuna basın: ")
                if choice == "q":
                    break
            



