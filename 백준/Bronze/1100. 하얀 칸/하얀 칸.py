import math
import sys
from collections import deque
import copy
import datetime

arr = [list(map(str, input())) for _ in range(8)]

result = 0
for i in range(0,8,2):
    for j in range(0,8,2):

        if arr[i][j] == 'F':
            result += 1

for i in range(1,8,2):
    for j in range(1,8,2):
        if arr[i][j] == 'F':
            result += 1
print(result)