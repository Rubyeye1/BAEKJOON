import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


n1, k1, n2, k2 = map(int, sys.stdin.readline().split())

print(n1*k1 + n2*k2)