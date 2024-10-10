import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

n = int(sys.stdin.readline())
S = list(map(str, list(sys.stdin.readline().rstrip())))

for i in range(len(S)):
    if S[i].isupper():
        S[i] = S[i].lower()
    else:
        S[i] = S[i].upper()

for i in range(len(S)):
    print(S[i], end="")