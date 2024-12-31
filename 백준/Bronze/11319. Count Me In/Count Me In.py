import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

S = int(sys.stdin.readline())

for _ in range(S):

    L = input()
    L = list(L)

    resultA = 0
    resultB = 0

    for i in range(len(L)):
        if L[i] == "a" or L[i] == "e" or L[i] == "i" or L[i] == "o" or L[i] == "u" or L[i] == "A" or L[i] == "E" or L[i] == "I" or L[i] == "O" or L[i] == "U":
            resultA += 1
        elif L[i] != " ":
            resultB += 1

    print(resultB, resultA)