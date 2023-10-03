# Nama          : Dengklek al ucupi
# NIM           : L0123(...)
# Prodi/Kelas   : Sastra Pertanian/E

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