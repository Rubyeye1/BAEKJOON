import math
import sys
from collections import deque
import copy
import datetime

L = input()
result = []

for i in L:
    if 'a' <= i and i <= 'z':
        i = ord(i) + 13
        if i >= 123:
            i -= 26
        result.append(chr(i))

    elif 'A' <= i and i <= 'Z':
        i = ord(i) + 13
        if i >= 91:
            i -= 26
        result.append(chr(i))

    else:
        result.append(i)

for i in range(len(result)):
    print(result[i], end="")