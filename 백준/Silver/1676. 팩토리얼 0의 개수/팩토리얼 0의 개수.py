import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
temp = 1
for i in range(N):
    temp = temp * (i+1)
L = list(map(int, str(temp)))

result = 0

for i in range(len(L), 0, -1):
    if L[i-1] == 0:
        result = result + 1
    else:
        break

print(result)