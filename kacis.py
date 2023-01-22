import random
ilk_sayi = int(input("İstediğiniz Sayının ilk aralığını girin : "))
ikinci_sayi = int(input("İstediğiniz Sayının ikinci aralığını girin: "))

print(f"{ilk_sayi} ile {ikinci_sayi} arasında bir sayı üretiliyor lütfen bekleyiniz...")
print("Üretilen Sayı =",random.randint(ilk_sayi,ikinci_sayi))