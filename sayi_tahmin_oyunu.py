import random

sayi = random.randint(1, 100)
hak = 7
print("1 ile 100 arasinda bir sayi tahmin ediniz.")

tahmin = int(input("tahmininiz:"))
while hak > 0:
        if tahmin < sayi:
            hak = hak - 1
            print("daha buyuk")
        elif tahmin > sayi:
            hak = hak - 1
            print("daha kucuk")

        else:
            print("tebrikler")
            break
        tahmin = int(input("yeni tahmin:"))
if hak == 0:
        print("haklariniz bitti")
        

    

