# Nama          : Ivan Wahyu Nugroho
# NIM           : L0123068
# Prodi/Kelas   : Informatika/B


# Pola 3
def ketupat(n):
    k = n-1
    for i in range(1, n+2, 2):
        print(" "*(k-i+1) + "* "*i)
    for j in range(n-2, 0, -2):
        print(" "*(k-j+1) + "* "*j)

x = int(input())

if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)