def ketupat(n):
    k = int((n+1)/2)
    for i in range(1, k+1):
        print(" "*(i-1) + "* "*(k-i+1))
    for j in range(k-1, 0, -1):
        print(" "*(j-1) + "* "*(k-j+1))

x = int(input())

if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)