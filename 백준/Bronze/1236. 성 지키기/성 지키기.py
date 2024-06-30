import math
import sys
from collections import deque
import copy
import datetime


N, M = map(int, sys.stdin.readline().split())

L = [list(map(str, input())) for _ in range(N)]

tempN = []
tempM = []
for i in range(N):
    for j in range(M):
        if L[i][j] == "X" and j not in tempN:
            tempN.append(j)

for i in range(M):
    for j in range(N):
        if L[j][i] == "X" and j not in tempM:
            tempM.append(j)


print(max(M - len(tempN), N - len(tempM)))