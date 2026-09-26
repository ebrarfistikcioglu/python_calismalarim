# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("en az 8 karakter")
#     elif not re.search("[a-z]",psw):
#         raise Exception("kucuk harf olmali")
#     else:
#        print("gecerli parola")
    
# password = "12345678"

# try:
#     check_password(password)
# except Exception as ex:
#  print(ex)
# else:
#    print("gecerli parola: else")

# liste =["1","2","5a","10b","abc"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# while True:
#     sayi = input("sayi:")
#     if sayi == "q":
#         break
#     try:
#         result = float(sayi)
#         print("girilen sayi",result)
#         break
#     except ValueError:
#         print("gecersiz")
#         continue

# turkce_karakterler = "şçöüıİ"
# parola = input("parola: ")
# try:
#     for i in parola:
#        if i in turkce_karakterler:
#         raise TypeError("turkce karakter girdiniz")
    
#     print("gecerli parola")
# except TypeError as err:
#   print(err)

# def check_password(psw):
#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError("turkce karakter girdiniz")
#     print("gecerli parola")
# try:
#     check_password(parola)
# except TypeError as err:
#     print(err)

# def faktoriyel(x):
#     x = int(x)
#     if x<0:
#         raise ValueError("negatif deger")
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result
# for x in [5, 10, -3, "10b"]:
#     try:
#        y = faktoriyel(x)
#     except ValueError as err:
#         print(err)
#         continue
#     print(y)

# file = open("newfile.txt", "w")
# file.write("Sadik")
# file = open("newfile.txt", "a",encoding="utf-8")
# file.write("Cinar\n")
# file.close()

def ortalama_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])

    ortalama = int((not1 + not2)/2)

    return ogrenciAdi+":"+str(ortalama)+"\n"

def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as f:
        for satir in f:
            print(ortalama_hesapla(satir))
def not_gir():
    ad = input("ad:")
    soyad = input("soyad:")
    not1 = input("1.not:")
    not2 = input("2.not")

    with open("sinav_notlari.txt","a",encoding="utf-8") as f:
        f.write(f"{ad} {soyad}:{not1},{not2}\n")
    print("not kaydedildi")

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as f:
        liste = []

        for i in f:
            liste.append(ortalama_hesapla(i))

        with open("sonuclar.txt","w",encoding="utf-8") as f2:
            for i in liste:
                f2.write(i)

while True:
    islem = input("1-Notlari oku\n2-Notlari gir\n3-Notlari kaydet\n4-Cikis\n")
    if islem == "1":
        notlari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kaydet()
    else:
        break


    



