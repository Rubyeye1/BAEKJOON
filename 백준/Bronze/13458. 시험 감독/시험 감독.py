import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
result = 0

for i in range(len(A)):

    A[i] -= B
    result += 1

    if A[i] > 0 and A[i] % C == 0:
        result += A[i] // C

    elif A[i] > 0 and A[i] % C != 0:
        result += (A[i] // C) + 1

print(result)