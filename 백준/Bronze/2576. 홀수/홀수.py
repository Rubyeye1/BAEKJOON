import sys

a = []
for i in range(7):
    temp = int(sys.stdin.readline())
    if temp % 2 == 1:
        a.append(temp)
if len(a) != 0:
    a.sort()

    min = a[0]
    hab = sum(a)

    print(hab)
    print(min)
else:
    print(-1)