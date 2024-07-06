import math
import sys
from collections import deque
import copy
import datetime

L = input()
result = 0

for i in L:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        result += 1

print(result)