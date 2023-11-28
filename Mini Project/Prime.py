# Kondisi untuk mengecek atau mendata bilangan prima
import os
os.system("cls")

print("\n ___ PROGRAM BILANGAN PRIMA ___ \n")
print("Pilih 1 jika Anda ingin mengecek sebuah bilangan prima atau bukan \nPilih 2 jika Anda ingin mendata semua bilangan prima pada interval yang Anda inputkan")
while True:
    masukan = int(input("Opsi : "))
    if masukan ==1:
        print("\n==== MENGECEK BILANGAN PRIMA ====")
        num = int(input("\n Masukkan sebuah bilangan bulat : "))
        if num>1:
            for i in range(2, num):
                if num%i==0:
                    print(num, "bukan bilangan prima")
                    break
            else:
                print(num, "adalah bilangan prima")
        else:
            print(num, "bukan bilangan prima")
    elif masukan ==2:
        print("\n ==== MENDATA BILANGAN PRIMA ====")
        num1 = int(input("Masukkan bilangan batas bawah : "))
        num2 = int(input("Masukkan bilangan batas atas : "))
        print("\n Bilangan prima dalam interval tersebut adalah :")
        for bil in range(num1, num2+1):
            if bil>1:
                for n in range(2, bil):
                    if bil%n ==0:
                        break
                else:
                    print(bil)
            elif num1<1 and num2<1:
                print("Tidak ada bilangan prima")
                break
    else:
        print("Upsss, masukan Anda salah")
    tanya = str(input(f'\n Apakah Anda ingin mengulangi program ini kembali? (y/n) : '))
    if tanya=="n":
        print("\n Program selesai, terima kasih")
        break
    elif tanya =="y":
        continue
    else:
        print("Upsss... Masukkan y atau n saja, jangan yang lain")
