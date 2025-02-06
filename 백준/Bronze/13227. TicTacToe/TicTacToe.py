import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = [list(map(str, input())) for _ in range(3)]

cnt = 0

if L[0][0] != "." and L[0][0] == L[0][1] and L[0][1] == L[0][2]:
    cnt += 1
elif L[1][0] != "." and L[1][0] == L[1][1] and L[1][1] == L[1][2]:
    cnt += 1
elif L[2][0] != "." and L[2][0] == L[2][1] and L[2][1] == L[2][2]:
    cnt += 1
elif L[0][0] != "." and L[0][0] == L[1][0] and L[1][0] == L[2][0]:
    cnt += 1
elif L[0][1] != "." and L[0][1] == L[1][1] and L[1][1] == L[2][1]:
    cnt += 1
elif L[0][2] != "." and L[0][2] == L[1][2] and L[1][2] == L[2][2]:
    cnt += 1
elif L[0][0] != "." and L[0][0] == L[1][1] and L[1][1] == L[2][2]:
    cnt += 1
elif L[0][2] != "." and L[0][2] == L[1][1] and L[1][1] == L[2][0]:
    cnt += 1

if cnt >= 1:
    print('YES')
else:
    print("NO")