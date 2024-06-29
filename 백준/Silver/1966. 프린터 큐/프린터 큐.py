import math
import sys
from collections import deque
import copy
import datetime

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    L = list(map(int, sys.stdin.readline().split()))
    L = deque(L)

    count = 0
    A = M

    while True:
        Max = max(L)
        temp = L.popleft()
        A -= 1

        if Max == temp:
            count += 1
            if A < 0:
                print(count)
                break

        else:
            L.append(temp)
            if A < 0:
                A = len(L) - 1