# NAMA : 
# NIM :
# KELAS :

x = int(input())

if x % 2 == 0:
    x -= 1

baris = x // 2 + 1
spasi = 0
tes = x

for i in range(baris, 1, -1):
    if spasi != 0:
        print(" " * spasi, end="")
    
    for j in range(1, tes + 1):
        if j % 2 == 0:
            print("   ", end="")
        else:
            print("*", end="")
    print()
    tes -= 2
    spasi += 2

baris2 = x // 2

for i in range(baris2 + 1):
    if spasi != 0:
        print(" " * spasi, end="")
    
    for j in range(1, tes + 1):
        if j % 2 == 0:
            print("   ", end="")
        else:
            print("*", end="")
    print()
    tes += 2
    spasi -= 2