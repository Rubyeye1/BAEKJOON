import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

H, M = map(int, sys.stdin.readline().split())

partH = H - 9

print(partH * 60 + M)