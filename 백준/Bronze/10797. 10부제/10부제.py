import math
import sys
from collections import deque
import copy

Bujae = int(input())
L = list(map(int, sys.stdin.readline().split()))


result = 0

for i in range(len(L)):
    if L[i] == Bujae:
        result += 1

print(result)