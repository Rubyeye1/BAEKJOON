import math
import sys
from collections import deque
import copy
import datetime

N, K = map(int, sys.stdin.readline().split())
L = []
for i in range(1, N+1):
    L.append(i)

result = []

while L:
    for i in range(K-1):
        temp = L.pop(0)
        L.append(temp)
    temp2 = L.pop(0)
    result.append(temp2)

print("<",end="")
print(", ".join(map(str, result)), end="")
print(">")