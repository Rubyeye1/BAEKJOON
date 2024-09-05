import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T, D, M = map(int, sys.stdin.readline().split())
L = []
chk = 0
result = 0

for _ in range(M):
    temp = int(sys.stdin.readline())
    L.append(temp)

if M == 0:
    if T <= D:
        print("Y")
    else:
        print("N")

else:
    result = L[0]
    if result >= T:
        print("Y")
        chk = 1

    if chk == 0:
        for i in range(M):

            if i == M-1:
                result = D - L[i]
            else:
                result = L[i+1] - L[i]

            if result >= T:
                print("Y")
                chk = 1
                break

        if chk == 0:
            print("N")