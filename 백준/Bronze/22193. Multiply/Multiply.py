import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N, M = map(int, sys.stdin.readline().split())

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

print(A * B)