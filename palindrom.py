import string

kelime = input("Bir kelime ya da cümle girin: ")

# Noktalama işaretlerini ve boşlukları kaldır, küçük harfe çevir
duzenlenmis = ''.join(char.lower() for char in kelime if char.isalnum())

if duzenlenmis == duzenlenmis[::-1]:
    print("Palindromdur")
else:
    print("Palindrom değildir")
