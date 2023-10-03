# Nama          : Dengklek al ucupi
# NIM           : L0123(...)
# Prodi/Kelas   : Sastra Pertanian/E

def ketupat(n):
    k = int((n+1)/2)
    for i in range(1, k):
        print(" "*(2*(i-1)) + "*" + " "*(2*n-4*i+1) + "*")
    print(" "*(n-1) + "*")
    for j in range(k-1, 0, -1):
        print(" "*(2*(j-1)) + "*" + " "*(2*n-4*j+1) + "*")
        
        

x = int(input())

if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)