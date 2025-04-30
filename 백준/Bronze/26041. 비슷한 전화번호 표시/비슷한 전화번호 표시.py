import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A = list(map(str, sys.stdin.readline().split()))
B = input()
result = 0
temp = len(B)

for i in range(len(A)):
    if A[i] != B:
        if A[i][:temp] == B:
            result += 1	

print(result)