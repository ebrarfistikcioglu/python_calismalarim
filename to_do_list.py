dosya = "tasks.txt"

try:
    with open(dosya, "r") as f:
        tasks = f.read().splitlines()
except FileNotFoundError:
    tasks = []
while True:
    print("\nTo Do List")
    print("1. Görevleri listele")
    print("2. Görev ekle")
    print("3. Görev sil")
    print("4. Kaydet ve çık")

    secim = input("Seçiminiz: ")

    if secim == "1":
        if not tasks:
            print("Görev yok")
        else:
            print("\nGörevler:")
            for i, gorev in enumerate(tasks, start=1):
                print(f"{i}. {gorev}")

    elif secim == "2":
        yeni = input("Yeni görev: ")
        tasks.append(yeni)
        print("Görev eklendi.")

    elif secim == "3":
        numara = int(input("Silmek istediğiniz görev numarası: "))
        try:
            1 <= numara <= len(tasks)
            silinen = tasks.pop(numara - 1)
            print(f"{silinen} silindi.")
        except:
            print("Geçersiz numara")

    elif secim == "4":
        with open(dosya, "w") as f:
            f.write("\n".join(tasks))
        print("Kaydedildi")
        break

    else:
        print("Hatalı seçim")




