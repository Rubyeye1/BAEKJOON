import math
import sys
from collections import deque
import copy
import datetime

YD = input()
N = int(sys.stdin.readline())
tempL = sorted([input() for _ in range(N)])

MaxResult = 0
MaxIndex = 0

for i in range(N):

    L = YD.count("L") + tempL[i].count("L")
    O = YD.count("O") + tempL[i].count("O")
    V = YD.count("V") + tempL[i].count("V")
    E = YD.count("E") + tempL[i].count("E")
    result = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

    if MaxResult < result:
        MaxResult = result
        MaxIndex = i

print(tempL[MaxIndex])