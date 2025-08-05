# carpim_tablosu.py

# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# 1'den 10'a kadar çarpım tablosunu yazdır
print(f"{sayi} sayısının çarpım tablosu:")
for i in range(1, 11):
    print(f"{sayi} x {i} = {sayi * i}")
