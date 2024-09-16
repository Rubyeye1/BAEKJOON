import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
K = int(sys.stdin.readline())

print(int(M / N * K))