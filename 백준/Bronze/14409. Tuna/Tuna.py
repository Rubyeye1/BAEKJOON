import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
X = int(sys.stdin.readline())
result = 0

for i in range(N):

    P1, P2 = map(int, sys.stdin.readline().split())

    if abs(P1-P2) <= X:
        if P1 > P2:
            result += P1
        else:
            result += P2

    else:
        P3 = int(sys.stdin.readline())
        result += P3

print(result)