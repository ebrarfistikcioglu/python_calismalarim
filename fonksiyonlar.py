# def sayHello(name = "user"):
#     print("hello " + name)
# sayHello("ebrar")

# def total(num1,num2):
#     return num1 + num2
# result = total(10,20)
# print(result)

# def yazdir(kelime,adet):
#     return kelime * adet
# sonuc = yazdir("merhaba\n" ,5)
# print(sonuc)

# def cevir(*params):
#     return list(params)
# print(cevir(10, 20,"ali"))

# def cevir(*params):
#     list = []
#     for param in params:
#         list.append(param)
#     return list
# print(cevir(10,20,"ali"))

# sayi1 = int(input("1.sayı:"))
# sayi2 = int(input("2.sayı:"))
# def bul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2 + 1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)
# bul(sayi1, sayi2)

# sayi = int(input("sayı:"))
# def tambolenler(sayi):
#     list = []
#     for i in range(1, sayi+1):
#         if sayi % i == 0:
#                 list.append(i)
#     return list
# print(tambolenler(sayi))

# numbers = [1,3,4,5,10]
# def check_even(num): return num%2==0
# print(list(filter(check_even,numbers)))

# check_even = lambda num : num % 2 == 0
# print(list(filter(check_even,numbers)))

# name = "çınar"
# def change_name(new_name):
#     name = new_name
#     print(name)
# change_name("ada")
# print(name)

AliHesap = {
    "ad" : "Ali Turan",
    "hesapno" : 123,
    "bakiye" : 2000,
    "ek" : 1000 
}

def paraCek(hesap, miktar):
    print(f"merhaba {hesap['ad']}")

    if hesap["bakiye"]>=miktar:
        hesap["bakiye"] -= miktar
        print("para cekilebilir.")
    else:
        toplam = hesap['bakiye'] + hesap['ek']

        if toplam >= miktar:
            ekhesap = input("ek hesap kullanilsin mi(e/h):")

            if ekhesap == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ek"] -= kullanilacakMiktar
                print("para hazir")
            else:
                print(f"{hesap['hesapno']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir")

        else:
            print("bakiye yetersiz")
             
paraCek(AliHesap, 4000)
paraCek(AliHesap, 3000)