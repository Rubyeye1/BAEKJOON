import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

week = 0

while True:

    N = int(sys.stdin.readline())
    if N == 0:
        break

    S = set()

    week += 1

    for _ in range(N):
        temp = input()
        S.add(temp)

    print("Week " + str(week) + " " + str(len(S)))