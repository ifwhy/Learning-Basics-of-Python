# Nama          : Ivan Wahyu Nugroho
# NIM           : L0123068
# Prodi/Kelas   : Informatika/B


# Pola 2
def kotak(x):
    for i in range(1, x+1):
        if i == 1 or i == (x+1)/2 or i == x:
            print("* "*x)
        else :
            print("* " + " "*(x-4) + " * " + " "*(x-4) + " *")

x = int(input())

if x%2 == 1:
    kotak(x)
else :
    kotak(x-1)
    