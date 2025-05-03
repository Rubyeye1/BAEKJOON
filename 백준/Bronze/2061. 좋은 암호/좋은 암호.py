import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

K, L = map(int, sys.stdin.readline().split())
ck = 0

for i in range(2, L):
    if K % i == 0:
        print("BAD", i)
        ck = 1
        break

if ck == 0:    
    print("GOOD")