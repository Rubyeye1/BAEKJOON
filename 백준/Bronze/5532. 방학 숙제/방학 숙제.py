import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

temp1 = 0
temp2 = 0

if A % C == 0:
    temp1 = A // C
else:
    temp1 = A // C + 1

if B % D == 0:
    temp2 = B // D
else:
    temp2 = B // D + 1

result = max(temp1, temp2)
print(L - result)