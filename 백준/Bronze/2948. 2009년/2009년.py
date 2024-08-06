import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime

D, M = map(int, sys.stdin.readline().split())

temp = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
result = temp[date(2009, M, D).weekday()]
print(result)