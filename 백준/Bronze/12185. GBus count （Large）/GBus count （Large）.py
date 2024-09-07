import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for t in range(T):

    N = int(input())
    result = list(map(int, sys.stdin.readline().split()))
    P = int(sys.stdin.readline())

    case = []

    for _ in range(P):
        cnt = 0
        temp = int(sys.stdin.readline())

        for i in range(0, len(result), 2):
            if result[i] <= temp <= result[i + 1]:
               cnt += 1
        case.append(cnt)
        
    print("Case #" + str(t+1) + ": ", end="")
    for x in case:
        print(x, end=" ")

    print("")
    a = input()