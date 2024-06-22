import math
import sys
from collections import deque
import copy
import datetime

N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
count = 0

while (start <= end and end <= N):
    temp = sum(L[start:end])

    if (temp < M):
        end += 1
    elif (temp > M):
        start += 1
    else:
        count += 1
        start += 1

print(count)