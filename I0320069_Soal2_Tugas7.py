def Abs():
    print("Anda memilih fungsi abs")
    a = int(input("Masukan bilangan negatif / positif variabel a = "))
    b = int(input("Masukan bilangan negatif / positif variabel b = "))
    print("a = ", a)
    print("b = ", b)
    print("\n|a|: ", abs(a))
    print("|b|: ", abs(b))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def ceil():
    import math
    print("Anda memilih fungsi ceil")
    a = float(input("Masukan bilangan riil variabel a = "))
    b = float(input("Masukan bilangan riil variabel b = "))
    print("a = ", a)
    print("b = ", b)
    print("\nmath a ceil: ", math.ceil(a))
    print("nilai a ceil: ", math.ceil(b))
    print("Perbedaan fungsi ceil dengan fungsi floor adalah")
    print("fungsi ceil membulatkan bilangan riil ke bilangan bulat diatasnya")
    print("sedangkan fungsi floor membulatkan bilangan riil ke bilanan bulat dibawahnya")
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def fabs():
    import math
    print("Anda memilih fungsi fabs")
    a = int(input("Masukan bilangan negatif / positif variabel a = "))
    b = float(input("Masukan bilangan riil negatif / positif variabel b = "))
    print("a = ", a)
    print("b = ", b)
    print("math.fabs a = ", math.fabs(a))
    print("math.fabs b = ", math.fabs(b))
    print("fungsi fabs memiliki tujuan hampir sama dengan fungsi abs")
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def floor():
    import math
    print("Anda memilih fungsi floor")
    a = float(input("Masukan bilangan riil variabel a = "))
    b = float(input("Masukan bilangan riil variabel b = "))
    print("a = ", a)
    print("b = ", b)
    print("math.floor a = ", math.floor(a))
    print("math.floor b = ", math.floor(b))
    print("Perbedaan fungsi floor dengan fungsi ceil adalah")
    print("fungsi floor membulatkan angka riil ke bilangan bulat dibawahnya")
    print("sedangkan fungsi ceil membulatkan angka riil ke bilangan bulat diatasnya")
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def min_max():
    print("Anda memilih fungsi min dan max")
    a = int(input("Masukan bilangan variabel a = "))
    b = int(input("Masukan bilangan variabel b = "))
    c = int(input("Masukan bilangan variabel c = "))
    d = int(input("Masukan bilangan variabel d = "))
    print("nilai min = ", min(a, b, c, d))
    print("nilai max = ", max(a, b, c, d))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def sqrt():
    import math
    print("Anda memilih fungsi sqrt")
    a = int(input("Masukan bilangan variabel a = "))
    b = int(input("Masukan bilangan variabel b = "))
    c = int(input("Masukan bilangan variabel c = "))
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("nilai sqrt a = ", math.sqrt(a))
    print("nilai sqrt b = ", math.sqrt(b))
    print("nilai sqrt c = ", math.sqrt(c))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def choice():
    import random
    print("Anda memilih fungsi choice")
    list = []
    print("Masukan 3 makanan yang anda inginkan")
    a = input("Makanan pertama = ")
    list.append(a)
    b = input("Makanan kedua = ")
    list.append(b)
    c = input("makanan ketiga = ")
    list.append(c)
    print("List makanan = ",list)
    print("Hasil random-nya adalah",random.choice(list))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def mulai():
    print("======= Pengenalan Fungsi Numerik =======")
    print('1. Fungsi Abs')
    print('2. Fungsi Ceil')
    print('3. Fungsi Fabs')
    print('4. Fungsi Floor')
    print('5. Fungsi Min dan Max')
    print('6. Fungsi Sqrt')
    print('7. Fungsi Choice')
    pilihan = input("Masukan nomor fungsi yang anda inginkan (1/2/3/4/5/6/7) = ")
    if pilihan == "1":
        Abs()
    elif pilihan == "2":
        ceil()
    elif pilihan == "3":
        fabs()
    elif pilihan == "4":
        floor()
    elif pilihan == "5":
        min_max()
    elif pilihan == "6":
        sqrt()
    elif pilihan == "7":
        choice()
    else:
        print("Input tidak valid")
        print("Masukan nomor pilihan 1 - 7")
    mulai()
mulai()