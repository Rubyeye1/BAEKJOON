import math
import sys
from collections import deque
import copy
import datetime


Number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = map(int, sys.stdin.readline().split())
result = []

while N:

    result.append(Number[N % B])
    N = N // B

for i in range(len(result)-1, -1, -1):

    print(result[i], end="")