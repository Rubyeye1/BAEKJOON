import math
import sys
from collections import deque
import copy
import datetime

a, b = map(int, sys.stdin.readline().split())

L1 = list(map(int, str(a)))
L2 = list(map(int, str(b)))

L3 = []
L4 = []
for i in reversed(range(len(L1))):
    L3.append(L1[i])
for i in reversed(range(len(L2))):
    L4.append(L2[i])


for i in range(len(L3)):
    if L3[i] == '0':
        L3.pop(0)
    else:
        break
for i in range(len(L4)):
    if L4[i] == '0':
        L4.pop(0)
    else:
        break

resultA = ''.join(map(str,L3))
resultB = ''.join(map(str,L4))
result = int(resultA) + int(resultB)

L5 = list(map(int, str(result)))

L6 = []
for i in reversed(range(len(L5))):
    L6.append(L5[i])

for i in range(len(L6)):
    if L6[i] == '0':
        L6.pop(0)
    else:
        break

finalResult = ''.join(map(str, L6))
print(int(finalResult))