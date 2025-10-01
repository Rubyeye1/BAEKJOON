import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

s1, s2 = map(int, sys.stdin.readline().split())

if s1 >= s2 / 2:
    print("E")
else:
    print("H")