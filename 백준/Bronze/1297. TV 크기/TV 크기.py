import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

D, H, W = map(int, sys.stdin.readline().split())

temp = D / math.sqrt(H * H + W * W)

print(int(H * temp), int(W * temp))