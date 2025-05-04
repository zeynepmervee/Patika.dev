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


# asal
sayi = int(input("Bir sayı girin: "))
if sayi > 1:
    for i in range(2, sayi):
        if sayi % i == 0:
            print("Asal değil")
            break
    else:
        print("Asal")
else:
    print("Asal değil")

sayi = int(input("Bir sayı girin: "))
i = 2
asal = True
if sayi > 1:
    while i < sayi:
        if sayi % i == 0:
            asal = False
            break
        i += 1
    print("Asal" if asal else "Asal değil")
else:
    print("Asal değil")

# index
notlar = [45, 85, 75, 50]
for i in range(len(notlar)):
    if notlar[i] == 75:
        print("75'in indeksi:", i)


# faktoriyel
sayi = int(input("Faktöriyeli alınacak sayı: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print("Faktöriyel:", faktoriyel)

sayi = int(input("Faktöriyeli alınacak sayı: "))
faktoriyel = 1
i = 1
while i <= sayi:
    faktoriyel *= i
    i += 1
print("Faktöriyel:", faktoriyel)

# pozitif gelene kadar for
for _ in range(100):  # sonsuz gibi çalışır
    sayi = int(input("Pozitif bir sayı girin: "))
    if sayi > 0:
        print("Tebrikler, pozitif sayı girdiniz:", sayi)
        break

# asal
def asal_mi(sayi):
    if sayi <= 1:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

sayi = int(input("Bir sayı girin: "))
print("Asal" if asal_mi(sayi) else "Asal değil")

# faktoriyel
def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

sayi = int(input("Faktöriyeli alınacak sayı: "))
print("Faktöriyel:", faktoriyel(sayi))