import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
S = input()
S = list(S)

for i in range(1, len(S)):
    if S[i] == "J":
        print(S[i-1])