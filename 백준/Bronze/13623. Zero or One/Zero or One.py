import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
    print("*")
elif a != b and a != c and b == c:
    print("A")
elif b != a and b != c and a == c:
    print("B")
elif c != a and c != b and a == b:
    print("C")