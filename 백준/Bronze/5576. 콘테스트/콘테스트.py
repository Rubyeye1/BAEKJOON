import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

W = []
K = []

for i in range(20):
    if i < 10:
        temp = int(sys.stdin.readline())
        W.append(temp)
    else:
        temp = int(sys.stdin.readline())
        K.append(temp)

W.sort(reverse = True)
K.sort(reverse = True)

print(sum(W[:3]), sum(K[:3]))