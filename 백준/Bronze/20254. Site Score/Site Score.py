import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


UR, TR, UO, TO = map(int, sys.stdin.readline().split())

print(56 * UR + 24 * TR + 14 * UO + 6 * TO)