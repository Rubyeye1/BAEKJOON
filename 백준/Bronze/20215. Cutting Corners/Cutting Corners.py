import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

w, h = map(int, sys.stdin.readline().split())

print(w+h - (math.sqrt(w*w + h*h)))