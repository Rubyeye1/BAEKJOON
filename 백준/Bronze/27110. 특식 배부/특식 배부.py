import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
A, B, C = map(int, sys.stdin.readline().split())

tempA = 0
tempB = 0
tempC = 0

if A <= N:
    tempA = A
else:
    tempA = N
if B <= N:
    tempB = B
else:
    tempB = N
if C <= N:
    tempC = C
else:
    tempC = N

print(tempA + tempB + tempC)