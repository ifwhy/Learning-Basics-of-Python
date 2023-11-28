# Nama          : Ivan Wahyu Nugroho
# NIM           : L0123068
# Prodi/Kelas   : Informatika/b


# Pola 8
def ketupat(n):
    k = n-1
    for j in range(n, 2, -2):
        print(" "*(k-j+1) + "* "*j)
    for i in range(1, n+2, 2):
        print(" "*(k-i+1) + "* "*i)

x = int(input())

if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)