sayi1 = input("Bir sayı giriniz:")
sayi1_int = int(sayi1)
sayi2 =input("Bir sayı daha giriniz:")
sayi2_int = int(sayi2)
islem = input("İşleminiz nedir? 'toplama' , 'çıkarma' , 'çarpma' , 'bölme': ")
if islem == "toplama":
    sonuc = sayi1_int + sayi2_int
    print(sonuc)
elif islem == "çıkarma":
    sonuc = sayi1_int - sayi2_int
    print(sonuc)
elif islem == "çarpma":
    sonuc = sayi1_int * sayi2_int
    print(sonuc)    
elif islem == "bölme":
    if sayi2_int == 0:
        print("ifade tanımsız")
    else:
        sonuc = sayi1_int / sayi2_int
        print(sonuc)
else:
    print("işlem başarısız")    

