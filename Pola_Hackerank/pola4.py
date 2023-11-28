# Nama          : Ivan Wahyu Nugroho
# NIM           : L0123068
# Prodi/Kelas   : Informatika/B

# Pola 4
def ketupat(n):
    k = int((n+1)/2)
    for i in range(1, k+1):
        spasi = 4*i-7
        bintang = int((2*n-1-spasi)/4)
        if i == 1:
            print("* "*(n))
        else :  
            print("* "*(bintang) + " "*(spasi) + " *"*(bintang))
    for j in range(k-1, 0, -1): 
        spasi = 4*j-7
        bintang = int((2*n-1-spasi)/4)
        if j == 1:
            print("* "*(n))
        else : 
            print("* "*(bintang) + " "*(spasi) + " *"*(bintang))
        
 
x = int(input())
 
if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)