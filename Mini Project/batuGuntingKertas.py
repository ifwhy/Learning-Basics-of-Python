import random as rd    

tanya = 1
while (tanya == 1) : 
    print("____PERMAINAN BATU GUNTING KERTAS DENGAN KOMPUTER____")
    print("\t Masukkan angka 1 untuk BATU")
    print("\t Masukkan angka 2 untuk GUNTING")
    print("\t Masukkan angka 3 untuk KERTAS")
    print("____________________________________________________")
    n = int(input("Pilih di sini : "))

    comp = rd.random()
    if comp <= 0.3333 :
        comp = 1
    elif comp > 0.3333 and comp <= 0.666:
        comp = 2
    else :
        comp = 3

    if n == 1:
        print("Anda memilih BATU")
    elif n == 2:
        print("Anda memilih GUNTING")
    elif n == 3:
        print("Anda memilih KERTAS")
    else:
        print("Masukan Anda salah")
        break

    if comp == 1:
        print("Komputer memilih BATU")
    elif comp == 2:
        print("Komputer memilih GUNTING")
    elif comp == 3:
        print("Komputer memilih KERTAS")

    print("Hasilnya adalah", end=" ")
    if n == comp :
        print("____SERI____")
    elif n == 1:
        if comp == 2:
            print("____ANDA MENANG____")
        elif comp == 3:
            print("____ANDA KALAH____")
    elif n == 2:
        if comp == 1:
            print("____ANDA KALAH____")
        elif comp == 3:
            print("____ANDA MENANG____")
    elif n == 3:
        if comp == 1:
            print("____ANDA MENANG____")
        elif comp == 2:
            print("___ANDA KALAH____")

    print()
    tanya = str(input("Apakah Anda ingin bermain lagi? (y/n): "))
    print()
    if tanya == 'y':
        tanya = 1
    elif tanya == 'n':
        tanya = 0
    else:
        print("Masukan Anda salah, program diakhiri")
        break
print("\t ____TERIMA KASIH SUDAH BERMAIN____")
print("\t \t ____SAMPAI JUMPA____")