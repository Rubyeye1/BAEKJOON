import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, Q = map(int, sys.stdin.readline().split())

Sigan = []
AkboSigan = []

for _ in range(N):
    temp = int(sys.stdin.readline())
    Sigan.append(temp)

for i in range(N):
    for j in range(Sigan[i]):
        AkboSigan.append(i+1)

for _ in range(Q):
    temp = int(sys.stdin.readline())
    print(AkboSigan[temp])