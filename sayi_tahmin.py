import random

def sayi_tahmin_oyunu():
    print("1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalış!")
    gizli_sayi = random.randint(1, 100)
    deneme_sayisi = 0

    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
            deneme_sayisi += 1

            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
            elif tahmin < gizli_sayi:
                print("Daha büyük bir sayı söyle.")
            elif tahmin > gizli_sayi:
                print("Daha küçük bir sayı söyle.")
            else:
                print(f"Tebrikler! {deneme_sayisi} denemede doğru tahmin ettiniz.")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    sayi_tahmin_oyunu()
