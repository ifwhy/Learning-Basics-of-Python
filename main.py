# Nama          : Dengklek al ucupi
# NIM           : L0123(...)
# Prodi/Kelas   : Sastra Pertanian/E

def ketupat(n):
    k = int((n+1)/2)
    for i in range(1, k+1):
        if i == 1:
            print("*" + " "*(n-2) + "*" + " "*(n-2) + "*")
        elif i == k:
            print("* "*(n))
        else :
            print(" "*(2*(i-1)) + "*" + " "*(n-2*i) + "*" + " "*(n-2*i) + "*" + " "*(2*i-1))
    for j in range(k-1, 0, -1):
       print(" "*(2*(j-1)) + "*" + " "*(n-2*j) + "*" + " "*(n-2*j) + "*" + " "*(2*j-1))
        
 
 
x = int(input())
 
if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)