"""
Soru1 
Metin Dosyası İşlemleri
Bir metin dosyasında satır satır saklanan sayıların toplamını ve ortalamasını hesaplayan bir program yazın.
Programınız aşağıdaki işlemleri gerçekleştirmelidir:

Kullanıcıdan dosya adı isteyin.
Dosyayı okuyun ve satırlardaki sayıları toplayın.
Toplam ve satır sayısını kullanarak ortalama değeri hesaplayın.
Sonuçları ekrana yazdırın.

"""
# texs_file.txt  dosyasi olusturduk ve arasinda sayilarin oldugu bir metin yazdik.
# texs_file.txt dosyasi ornegi.
# 1 - Amsterdam nufus 700 bin.
# 2 - Rotterdam nufus 500 bin den 1 az fazla.
# 3 - Utrech nusuf 1 milyona yakin. 

while True :
    textname = input(" dosya ismi yaz   : ")
    if textname != "text_file":
        print("Yanlis dosya ")  
    else: 
        print("Dosya aciliyor")
        with open("text_file.txt","r+",encoding="utf-8") as file : 
            text_file=file.read()
            print(text_file)
            numbers= [ int (num) for num in text_file.split(" ") if num.isdigit()]
            total_sum= sum(numbers)
            line_count= text_file.count("\n")+1
            average = total_sum/line_count
            print(f"Sayilarin toplami :{total_sum}'dir.Metinde {line_count} satir vardir. ")
            print("Sayilarin ortalamasi :",average)
            

            
        break
   
# Bu odevde icinde bir text bulunan text_file dosyasi olusturduk.Kullanicidan bu dosyanin adini yazarak acmasini istedik. 
# Acilan dosyadaki textin icindeki sayilari tespit edip bunlari topladik. Sonra textin kac satirdan olustugunu bulduk .
# Son olarak sayilar tolamini satir sayisina bolduk ve sonucu yazdirdik. 
"""


Soru 2:
Dosya Düzenleme
Bir metin dosyasındaki her satırın başına satır numarası ekleyen bir program yazın. 
Programınız aşağıdaki işlemleri gerçekleştirmelidir:

Kullanıcıdan dosya adı isteyin.
Dosyayı okuyun ve her satırın başına satır numarası ekleyin.
Dosyayı güncellenmiş içerikle tekrar yazın.

 Bu program, input fonksiyonunu kullanarak kullanıcıdan dosya adını alır. 
Ardından with blokları kullanarak dosyayı açar, okur ve tekrar yazar. 
İlk with bloğu, dosyayı okuyarak lines listesine satırları depolar. 
Daha sonra, ikinci with bloğu, dosyayı yazarak her satırın başına satır numarası ekler. 
enumerate fonksiyonu her satırın başına bir numara ekler ve her satırı write fonksiyonuyla güncellenmiş dosyaya yazar.        
       
Not: Bu program, dosyanın mevcut içeriğini değiştirecektir. 
Dosyanın içeriğini yedeklemek istiyorsanız, önce orijinal dosyayı başka bir dosyaya kopyalayabilirsiniz.





"""
# texs_file.txt dosyasi ornegi.
# Amsterdam nufus 700 bin.
# Rotterdam nufus 500 bin den 1 az fazla.
# Utrech nusuf 1 milyona yakin. 
while True :
    textname = input(" dosya ismi yaz   : ")
    if textname != "text_file":
        print("Yanlis dosya ")  
    else: 
        print("Dosya aciliyor")
        with open('text_file.txt', 'r',encoding ="utf-8") as f:
            lines = f.readlines()

            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")
    break            
