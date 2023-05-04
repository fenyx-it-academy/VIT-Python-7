
# Bir metin dosyasındaki her satırın başına satır numarası ekleyen bir program yazın.
# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve her satırın başına satır numarası ekleyin.
# # Dosyayı güncellenmiş içerikle tekrar yazın.

user=input("Dosya adi giriniz: ")

with open(user+".txt", "r") as dosya:

        words = dosya.read().split()
        print(words)

number = 1
with open(user+".txt", "w") as dosya:

        for i in words:
                dosya.writelines(str(number)+"-"+i+"\n")
                number += 1

with open(user+".txt", "r") as dosya:

        print(dosya.read())