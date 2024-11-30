import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

P = int(sys.stdin.readline())

temp = 100 - P

result25 = 0
result10 = 0
result5 = 0
result1 = 0

while True:
    if temp >= 25:
        temp -= 25
        result25 += 1
    else:
        break
while True:
    if temp >= 10:
        temp -= 10
        result10 += 1
    else:
        break
while True:
    if temp >= 5:
        temp -= 5
        result5 += 1
    else:
        break
while True:
    if temp >= 1:
        temp -= 1
        result1 += 1
    else:
        break

print(result25, result10, result5, result1)