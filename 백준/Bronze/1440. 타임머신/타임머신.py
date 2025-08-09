import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

L = list(map(int, sys.stdin.readline().split(':')))
h = [h for h in range(1,13)]
s = [s for s in range(60)]

result = 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                if L[i] in h and L[j] in s and L[k] in s:
                    result += 1

print(result)