import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b = map(int, sys.stdin.readline().split())

temp = a
result = 1

while True:
    if temp > b:
        break

    L = 0
    for i in range(temp):
         L += i+1

    result *= L
    temp += 1

print(result % 14579)