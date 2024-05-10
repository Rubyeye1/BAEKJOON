import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())

Munja = list(input())
for i in range(N-1):
    tempMunja = list(input())
    for j in range(len(Munja)):
        if Munja[j] != tempMunja[j]:
            Munja[j] = "?"

for i in range(len(Munja)):
    print(Munja[i], end="")