def ketupat(n):
    for i in range(1, n+2, 2):
        k = n-1
        if i == 1:
            print(" "*(k) + "*"*i)
        else :
            print(" "*(k-i+1) + "* "*i)
    for j in range(n-2, 0, -2):
        if j != 1:
            print(" "*(k-j+1) + "* "*j)
        else :
            print(" "*k + "*"*j)

x = int(input())

if x%2 == 1:
    ketupat(x)
else :
    ketupat(x-1)