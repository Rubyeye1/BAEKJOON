import sys

T = int(sys.stdin.readline())
a = []
b = []

for i in range(T):
     c, d = map(int, input().split())
     a.append(c)
     b.append(d)

for i in range(len(a)):
    temp = a[i] % 10
    if temp == 0:
        print(10)
    elif temp == 1 or a == 5 or a == 6:
        print(temp)
    elif temp == 4 or temp == 9:
        b[i] = b[i] % 2
        if b[i] == 1:
            print(temp)
        else:
            print((temp * temp) % 10)

    else:
        if b[i] % 4 == 0:
            print(temp ** 4 % 10)
        else:
            print(temp ** (b[i] % 4) % 10)