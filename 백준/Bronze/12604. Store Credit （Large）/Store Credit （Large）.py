import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for h in range(N):

    C = int(sys.stdin.readline())
    I = int(sys.stdin.readline())
    L = list(map(int, sys.stdin.readline().split()))

    resultK = 0
    resultJ = 0

    for k in range(I):
        for j in range(k+1, I):
            if (L[k] + L[j]) == C:
                resultK = k+1
                resultJ = j+1
                break

    print("Case #" + str(h+1) + ": " + str(resultK) + " " + str(resultJ))