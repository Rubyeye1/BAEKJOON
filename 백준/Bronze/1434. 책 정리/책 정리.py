import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

for i in range(len(B)):
    for j in range(len(A)):
        if B[i] > A[j]:
            continue
        A[j] -= B[i]
        break

print(sum(A))