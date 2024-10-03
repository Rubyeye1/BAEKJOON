import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b, c = map(int, sys.stdin.readline().split())

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print(a*b*c)
elif a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
    print(a*b*c)
elif a % 2 == 1 and b % 2 == 0 and c % 2 == 0:
    print(a)
elif a % 2 == 0 and b % 2 == 1 and c % 2 == 0:
    print(b)
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 1:
    print(c)
elif a % 2 == 1 and b % 2 == 1 and c % 2 == 0:
    print(a*b)
elif a % 2 == 1 and b % 2 == 0 and c % 2 == 1:
    print(a*c)
elif a % 2 == 0 and b % 2 == 1 and c % 2 == 1:
    print(b*c)