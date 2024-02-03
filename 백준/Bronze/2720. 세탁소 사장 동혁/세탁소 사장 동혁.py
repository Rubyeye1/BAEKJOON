import sys
from collections import deque                                       

T = int(sys.stdin.readline())

for i in range(T):
    temp = int(sys.stdin.readline())
    Q = 0
    D = 0
    N = 0
    P = 0
    if temp >= 25:
        Q = int(temp / 25)
        temp = temp - Q * 25
    if temp >= 10:
        D = int(temp / 10)
        temp = temp - D * 10
    if temp >= 5:
        N = int(temp / 5)
        temp = temp - N * 5
    if temp >= 1:
        P = int(temp / 1)
        temp = temp - P * 1

    print(Q, D, N, P)