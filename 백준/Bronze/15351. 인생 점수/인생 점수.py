import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

for _ in range(N):
    temp = input()
    result = 0

    for i in temp:
        if i == " ":
            continue
        tempscore = ord(i) - 64
        result += tempscore

    if result == 100:
        print('PERFECT LIFE')
    else:
        print(result)