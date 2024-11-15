import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

H1, B1 = map(int, sys.stdin.readline().split())
H2, B2 = map(int, sys.stdin.readline().split())

result1 = H1 * 3 + B1 * 1
result2 = H2 * 3 + B2 * 1

if result1 > result2:
    print(1, result1-result2)
elif result2 > result1:
    print(2, result2-result1)
else:
    print("NO SCORE")