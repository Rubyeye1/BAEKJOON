import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N  = list(map(int, sys.stdin.readline().split()))
temp = N.copy()
temp.sort()

if N == temp:
    print("Good")
else:
    print("Bad")