import math
import sys
from collections import deque
import copy
import datetime

N,M = map(int, sys.stdin.readline().split())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

K = int(sys.stdin.readline())
for q in range(K):
    result = 0
    i, j, x, y = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    for w in range(i, x+1):
        for e in range(j, y+1):
            result += L[w][e]

    print(result)