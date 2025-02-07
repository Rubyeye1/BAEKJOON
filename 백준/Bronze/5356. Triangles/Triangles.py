import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

N = int(sys.stdin.readline())

for _ in range(N):
    
    a, b = map(str, input().split())
    a = int(a)

    temp = L.index(b)

    for i in range(a):
        print(L[temp] * (i+1))

        temp += 1

        if temp == 26:
            temp = 0

    print()