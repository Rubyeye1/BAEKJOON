import math
import sys
from collections import deque
import copy
import datetime

T, S = map(int, sys.stdin.readline().split())
if S == 1 or (T <= 11 or T >= 17):
    print(280)
elif S == 0 and (T >= 12 or T <= 16):
    print(320)
