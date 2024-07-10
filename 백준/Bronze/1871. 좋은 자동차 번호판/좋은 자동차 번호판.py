import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())

for i in range(N):
    L, D = input().split("-")

    tempResult = 0
    for i in range(3):
        tempResult += (ord(L[i]) - 65) * (26 ** (2 - i))

    if abs(tempResult-int(D)) <= 100:
        print("nice")
    else:
        print("not nice")