# Nama          : Ivan Wahyu Nugroho
# NIM           : L0123068
# Prodi/Kelas   : Informatika/b


# Pola 7
def ketupat(n):
    k = int((n+1)/2)
    for i in range(1, k):
        print("* "*i + " "*(2*x-1-4*i) + " *"*i)
    print("* "*n)
    for j in range(k-1, 0, -1):
        print("* "*j + " "*(2*x-1-4*j) + " *"*j)
        

x = int(input())

if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)