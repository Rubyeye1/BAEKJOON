import math
import sys
from collections import deque
import copy

T = int(sys.stdin.readline())

for i in range(T):

    A, B = map(int, sys.stdin.readline().split())
    result = 0
    if A == 0:
        result += 0
    elif A == 1:
        result += 5000000
    elif A <= 3:
        result += 3000000
    elif A <= 6:
        result += 2000000
    elif A <= 10:
        result += 500000
    elif A <= 15:
        result += 300000
    elif A <= 21:
        result += 100000

    if B == 0:
        result += 0
    elif B == 1:
        result += 5120000
    elif B <= 3:
        result += 2560000
    elif B <= 7:
        result += 1280000
    elif B <= 15:
        result += 640000
    elif B <= 31:
        result += 320000

    print(result)