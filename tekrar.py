# website = "http://www.sadikturan.com" 
# course = "Python Kursu : Bastan Sona Python Programlama Rehberiniz (40 saat)"

# result = len(course)
# print(result)

# result = website[7:10]
# print(result)
# length = len(website)
# result = website[length-3:length]
# print(result)
# result1 = course[ :15]
# result2 = course[-15:]

# print(result1 + result2)

# name = "Bora"
# surname ="Yilmaz"
# age = "32"
# job = "Muhendis"
# print("Benim adim {} {}, yasim {}, meslegim {}".format(name,surname,age,job))

# s = "Hello world"
# s = s[0:6] + "W"+s[7:]
# print(s)

# result = "abc"
# print(result*3)

# message = "Hello There. My Name Is Sadik Turan"
# # index = message.find("Sadik")
# # print(index)

# isFound = message.startswith("H")
# print(isFound)

# result = website.lstrip("htp:/.w").rstrip(".com")
# print(result)

# message = course.replace("P","p").replace("K","k").replace("B","b").replace("S","s").replace("R","r")
# print(message)

# result = website.count("a")
# print(result)

# isFound = website.find(".com")
# print(isFound)

# isalpha = course.isalpha()
# print(isalpha)

# result = "contents".center(50,"*")
# print(result)

# result = course.replace("","-")
# print(result)

# result = "Hello World".replace("World","There")
# print(result)

# result = course.split(" ")
# print(result)

# cars = ["bmw", "mercedes", "opel", "mazda"]
# result = cars[::-1]
# print(result)

# studenta = ["Yigit Bilgi", "2010",[70,60,70]]
# studentb = ["Sena Turan","1999", [80,80,70]]
# result = f"{studenta[0]} {2026-int(studenta[1])} yasinda ve not ortalamasi {(studenta[2][0]+studenta[2][1]+studenta[2][2])/3}"
# print(result)

# names = ["A", "Y","H","D"]
# years = ["98", "2000", "98", "87"]
# names.append("C")
# val = max(years)
# val = min(years)
# print(val)

# result = years.count("98")
# print(result)

# years.clear()
# print(years)

# markalar = []
# marka = input("marka:")
# markalar.append(marka)
# print(markalar)

# ogrenciler = {}
# number = input("ogrenci no:")
# name = input("ogrenci ad:")
# surname = input("ogrenci soyad:")
# phone = input("ogrenci telefon:")
# ogrenciler.update({
#     number:{
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
#     }
# })
# print(ogrenciler)

# ogrNo= input("ogrenci no:")
# ogrenci = ogrenciler[ogrNo]
# print(ogrenci)

# print("*"*50)
# print(f"aradiginiz {ogrNo} nolu ogrencinin adi {ogrenci["ad"]} ve soyadi {ogrenci["soyad"]} telefon numarasi ise {ogrenci["telefon"]}")

# x, y, z = 2, 5, 10
# numbers = 1, 5, 7, 10, 6
# sayi1 = int(input("bir sayi giriniz:"))
# sayi2 = int(input("baska bir sayi daha giriniz:"))
# islem = int(sayi1*sayi2)
# sonuc = x + y + z
# print(int(sonuc-islem))

# islem = y**x
# x, *y, z = numbers
# islem = y[0]+y[1]+y[2]
# print(islem)

# sayi1 = int(input("1. sayi:"))
# sayi2 = int(input("2.sayi:"))
# result = sayi1 < sayi2
# print(f"{sayi1} {sayi2} den kucuk : {result}")

# vize1 = float(input("1. vize:"))
# vize2 = float(input("2.vize:"))
# final = float(input("final:"))
# ortalama = ((( vize1 + vize2 )/2)*0.6+(final)*0.4)
# result = (final>=70) or (ortalama >= 50)
# print(f"ortalamaniz {ortalama} ve sinavdan gecme durumunuz {result}")

# sayi = int(input("bir sayi giriniz:"))
# result = (sayi > 0)
# print(f"{sayi} pozitif ise {result}")

# email = "email@sadikturan.com"
# parola = "abc123"
# mail = input("e posta:")
# password = input("sifre:")
# result1 = email == mail
# result2 = parola == password
# print(f"{email} ile {mail} ayni ise {result1} {parola} ile {password} ayni ise {result2}")

# x = int(input("Sayi:"))
# result = (x > 0) and (x % 2 == 0)
# print(result)

# mail = "email@sadikturan"
# password = "abc123"
# x = input("eposta: ")
# y = input("sifre:")
# result = ( mail == x) and (password == y)
# print(f"mail ve password uyumlu: {result}")

# x = int(input("1.sayi: "))
# y = int(input("2.sayi:"))
# z = int(input("3.sayi: "))
# result = (x>y) and (x>z)
# print(f"x en buyuk sayidir: {result}")

# ad = input("isim:")
# kilo = float(input("kilo:"))
# boy = float(input("boy:"))
# indeks = (kilo)/ (boy**2)
# if 0<=indeks and indeks<=18.4:
#     print("zayif")
# elif 18.5<=indeks and indeks<=24.9:
#     print("normal")
# else:
#     print("haydi spora")        

# isim = input("ad: ")
# yas = int(input("yas: "))
# egitim = input("egitim: ")
# if yas >= 18:
#     if egitim == "lise" or egitim == "universite":
#         print(f"{isim} {yas} yasinda ve egitim durumu {egitim} oldugu icin ehliyet alabilir")
#     else:
#         print(f"{isim} {yas} yasinda fakat egitim durumu {egitim} oldugundan ehliyet uygun degil")
# else:
#     print("ehliyet uygun degil")

# yazili1 = float(input("1. yazili notu: "))
# yazili2 = float(input("2.yazili notu: "))
# sozlu = float(input("sozlu notu: "))
# ortalama = (yazili1 + yazili2 + sozlu)/3
# if ortalama >= 0 and ortalama <= 24:
#     print("not: 0")
# elif ortalama >= 25 and ortalama <= 44:
#     print("not: 1")
# else:
#     print("not: >=2")        

# x = float(input("sayi: "))
# # if 0<x and x<=100:
# #     print("sayi 0-100 arasinda")
# # else:
# #     print("sayi 0-100 arasinda degil") 
# if x>0:
#     if x % 2 == 0:
#         print("sayi pozitif ve cift")
#     else:
#         print("sayi pozitif ama cift degil")
# elif x <= 0:
#     if x % 2 == 0:
#         print("sayi pozitif degil ama cift")
#     else:
#         print("sayi hem pozitif degil hem tek")        
# 
# mail = input("e posta: ")
# password = input("sifre: ")
# if mail.strip() == "email@sadikturan.com":
#     if password == "abc123":
#         print("giris bilgileri dogru")
#     else:
#         print("e posta doğru ama sifre uyusmuyor")
# else:
#     print("giris bilgileri yanlis")  
# a = float(input("1. sayi:"))
# b = float(input("2.sayi: "))
# c = float(input("3.sayi: "))
# if a > b and a > c:
#     print("a en buyuk sayi")
# elif b > a and b > c:
#     print("b en buyuk sayi")
# else:
#     print("c en buyuk sayi")   
   
# if ortalama >= 50:
#      if final >= 50:
#          print(f"ortalama {ortalama} ve sinavdan gecti")
#      else:
#          print("final notu yetersiz")
# elif final >= 70:
#     print("gecti")
# else:
#     print(f"ortalama {ortalama} oldugu icin sinavdan kaldi")  

# sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# for sayi in sayilar:
#     if sayi%3==0:
#         print(sayi)

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)

# for sayi in sayilar:
#     if sayi%2==1:
#         print(sayi **2)

# sehirler = ["kocaeli","istanbul","ankara","rize"]
# for sehir in sehirler:
#     if len(sehir) <= 5:
#       print(sehir)

# urunler = [
#     {"name": "Samsung S6" , "price": 3000},
#     {"name": "S7" , "price": 4000},
# ]
# toplam = 0
# for urun in urunler:
#     fiyat = urun["price"]
#     toplam += fiyat
# print(toplam)
 
# for urun in urunler:
#     if int(urun["price"])<=4000:
#         print(urun["name"])

# x = 1
# while x <=100:
#     if x % 2 == 1:
#         print(f"{x} tek")
#     else:
#         print(f"{x} cift")
#     x += 1    

# name = ""
# while not name.strip():
#     name = input("isim:" )
# print(f"merhaba {name}")   

# for sayi in sayilar:
#     if sayi % 3==0:
#         print(sayi)

# baslangic = int(input("baslangic:"))
# bitis = int(input("bitis:"))
# i = baslangic
# while i < bitis:
#     i += 1
#     if i % 2 == 1:
#         print(i)
# print("son")

# # while True:
# #     sayi = int(input("Sayi gir: "))

# #     if sayi == 0:
# #         break

# #     print(sayi)

# sayilar = [ 1, 3, 5, 7, 9, 10]
# i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1

# i = 100
# while i>0:
#     i -= 1
#     print(i)

# numbers = []
# i = 0
# while i < 5:
#     sayi = int(input("sayi:"))
#     numbers.append(sayi)
#     i += 1
#     numbers.sort()
# print(numbers)    

# urunler = []
# adet = int(input("kac tane:"))
# i = 0
# while i < adet:
#     name = input("urun ismi:")
#     price = input("urun fiyati:")
#     urunler.append({
#         "isim" : name,
#         "fiyat" : price,
#     })
#     i += 1
# for urun in urunler:
#     print(f"urun adi {urun["isim"]} urun fiyati {urun["fiyat"]}")

# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1

# x = 1
# result = 0
# while x < 100:
#     if x % 2 == 1:
#         result += x
#     x += 1       
        
# print(result)
    
# x = 0
# result = 0
# while x < 100:
#     x += 1
#     if x % 2 == 0:
#         continue
#     result += x
# print(result)

# for item in range(2,10):
#     print(item)
# print(list(range(2,10)))

# index = 0
# greeting = "hello"
# # for letter in greeting:
# #     print(f"index: {index} letter: {greeting[index]}")
# #     index += 1
# for index,item in enumerate(greeting):
#     print(index,item)

# myString = "hello"
# myList = []
# for letter in myString:
#     myList.append(letter)
# print(myList)
# myList = [letter for letter in myString]
# print(myList)

# years = [1999, 2000, 2001]
# ages = [ 2026 - age for age in years]
# print(ages)

# result = [(x,y) for x in range(3) for y in range(3)]
# print(result)
