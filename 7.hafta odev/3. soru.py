import json

with open("student.json","r") as dosya:
    
    dict_dosya=json.load(dosya)
    
    count=len(dict_dosya)
    secim=input("Ogrencileri goruntulemekicin '1'\nOgrenci eklemek icin '2'")
    if secim=="1":
        for i in dict_dosya.values():
            print(i) 
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
                
                dict_dosya[f"student{count}"]=kayit
            with open("student.json","w") as dosya:
                json.dump(dict_dosya,dosya,indent=4)

                choice = input("Yeni öğrenci kaydı için 'Enter', çıkmak için 'q' tuşuna basın: ")
                if choice == "q":
                    break
            



