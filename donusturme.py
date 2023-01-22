import datetime
dogum = int(input("Doğduğunuz Yılı Girin:"))
suan = datetime.datetime.now()
yıl = suan.year
yas = yıl -dogum 
print(f"Yaşınız = {yas}")


#ilk_sayi = int(input("İlk Sayıyı Girin:"))
#ikinci_sayi = int(input("İkinci sayıyı girin:"))
#toplam = ilk_sayi + ikinci_sayi
# print("Sayınızın Toplamı = ",toplam)
#print(f"Sayılarınızın Toplamı = {toplam}")