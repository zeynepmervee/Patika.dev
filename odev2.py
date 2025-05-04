# pozitif - negatif
sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif bir sayı.")
elif sayi < 0:
    print("Negatif bir sayı.")
else:
    print("Sayı sıfır.")


# tek - cift
sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print("Çift sayı.")
else:
    print("Tek sayı.")

# harf notu
not_degeri = int(input("Notunuzu girin (0-100 arası): "))

if 80 <= not_degeri <= 100:
    print("Harf Notu: A")
elif 60 <= not_degeri < 80:
    print("Harf Notu: B")
elif 40 <= not_degeri < 60:
    print("Harf Notu: C")
elif 20 <= not_degeri < 40:
    print("Harf Notu: D")
elif 0 <= not_degeri < 20:
    print("Harf Notu: F")
else:
    print("Geçersiz not!")


# uzun - kisa isim
isim = input("Adınızı girin: ")

if len(isim) > 5:
    print("Uzun bir isminiz var.")
else:
    print("İsminiz:", isim)
