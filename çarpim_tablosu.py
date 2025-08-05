# liste_islemleri.py

sayilar = []

# Kullanıcıdan 5 adet sayı alınır
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

# Toplam, en küçük ve en büyük değer hesaplanır
toplam = sum(sayilar)
en_kucuk = min(sayilar)
en_buyuk = max(sayilar)

# Sonuçlar yazdırılır
print(f"Toplam: {toplam}")
print(f"En küçük sayı: {en_kucuk}")
print(f"En büyük sayı: {en_buyuk}")
