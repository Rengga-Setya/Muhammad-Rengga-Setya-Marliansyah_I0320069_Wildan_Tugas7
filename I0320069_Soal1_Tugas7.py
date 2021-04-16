def capitalize():
    print("Anda memilih fungsi capitalize")
    str = input("Masukan kata yang anda inginkan = ")
    print("Hasilnya adalah",str.capitalize())
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def center():
    print("Anda memilih fungsi center")
    str = input("Masukan kata yang anda inginkan = ")
    print("Hasilnya")
    s = str.center(30,'*')
    print(s)
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def count():
    print("Anda memilih fungsi count")
    str = input("Masukan kata yang anda inginkan = ")
    x = input("Masukan huruf yang ingin anda cari dari kata yang sudah dimasukan = ")
    print("Jumlah huruf",x,"adalah",str.count(x))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def endswith():
    print("Anda memilih fungsi endswith")
    str = input("Masukan 2 kata yang anda inginkan = ")
    x = input("Masukan kata pertama dari kata yang sudah dimasukan = ")
    y = input("Masukan kata kedua dari kata yang sudah dimasukan = ")
    print("Kata kedua dari", str, "adalah", y, str.endswith(y))
    print("Kata kedua dari",str,"adalah",x,str.endswith(x))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def find():
    print("Anda memilih fungsi find")
    str = input("Masukan 2 kata yang anda inginkan = ")
    x = input("Masukan huruf yang ingin anda cari indexnya = ")
    print("Huruf",x,"pada index",str.find(x))
    print("Perbedaan dari fungsi find dengan fungsi index")
    print("adalah output nilai yang tidak ditemukan")
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def index():
    print("Anda memilih fungsi index")
    str = input("Masukan 2 kata yang anda inginkan = ")
    x = input("Masukan huruf yang ingin anda cari indexnya = ")
    print("Huruf", x, "pada index", str.index(x))
    print("Perbedaan dari fungsi index dengan fungsi find")
    print("adalah output nilai yang tidak ditemukan")
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def replace():
    print("Anda memilih fungsi replace")
    str = input("Masukan 2 kata yang anda inginkan = ")
    x = input("Masukan kata yang ingin anda ganti dari kata yang sudah dimasukan = ")
    y = input("Masukan kata gantinya = ")
    print(str,"menjadi",str.replace(x,y))
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def upper_lower():
    print("Anda memilih fungsi upper dan lower")
    str = input("Masukan kata yang anda inginkan = ")
    print("Jika menggunakan fungsi upper = ",str.upper())
    print("Jika menggunakan fungsi lower = ",str.lower())
    ulang = input("Ulangi program? (y/t) = ")
    if ulang == "y":
        mulai()
    elif ulang == "t":
        print("Terima kasih sudah menggunakan program ini")
def mulai():
    judul = "Pengenalan Fungsi String"
    judul.center(50,"=")
    print(judul.center(50,"="))
    print('1. Fungsi Capitalize')
    print('2. Fungsi Center')
    print('3. Fungsi Count')
    print('4. Fungsi Endswith')
    print('5. Fungsi Find')
    print('6. Fungsi Index')
    print("7. Fungsi Replace")
    print("8. Fungsi Upper dan Lower")
    pilihan = input("Masukan nomor fungsi yang anda inginkan (1/2/3/4/5/6/7/8) = ")
    if pilihan == "1":
        capitalize()
    elif pilihan == "2":
        center()
    elif pilihan == "3":
        count()
    elif pilihan == "4":
        endswith()
    elif pilihan == "5":
        find()
    elif pilihan == "6":
        index()
    elif pilihan == "7":
        replace()
    elif pilihan == "8":
        upper_lower()
    else:
        print("Input tidak valid")
        print("Masukan nomor pilihan 1 - 8")
        mulai()
mulai()