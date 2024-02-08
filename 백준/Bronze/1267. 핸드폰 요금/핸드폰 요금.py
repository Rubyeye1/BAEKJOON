import math
import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
Yeong = 0
Min = 0
for i in range(N):
    temp = L[i]
    while temp >= 0:
        if temp >= 0:
            temp = temp - 30
            Yeong = Yeong + 10
        else:
            break

for i in range(N):
    temp = L[i]
    while temp >= 0:
        if temp >= 0:
            temp = temp - 60
            Min = Min + 15
        else:
            break

if Yeong == Min:
    print("Y M", Min)
elif Yeong < Min:
    print("Y", Yeong)
else:
    print("M", Min)