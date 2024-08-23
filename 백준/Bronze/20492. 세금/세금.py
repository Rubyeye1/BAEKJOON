import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


temp = int(sys.stdin.readline())

print(int(temp * 0.78), int(temp * 0.8 + temp * 0.2 * 0.78))