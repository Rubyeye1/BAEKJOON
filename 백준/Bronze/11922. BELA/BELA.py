import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


N, B = map(str, sys.stdin.readline().split())
N = int(N)
result = 0

for i in range(4 * N):
    temp = input()
    temp = list(temp)

    if temp[0] == "A":
        result += 11
    elif temp[0] == "K":
        result += 4
    elif temp[0] == "Q":
        result += 3
    elif temp[0] == "J":
        if temp[1] == B:
            result += 20
        else:
            result += 2
    elif temp[0] == "T":
        result += 10
    elif temp[0] == "9":
        if temp[1] == B:
            result += 14

print(result)