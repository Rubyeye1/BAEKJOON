import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

S = input()
S = list(S)

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    temp = S[a]
    S[a] = S[b]
    S[b] = temp

for i in range(len(S)):
    print(S[i], end="")