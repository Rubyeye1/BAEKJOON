import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

H = int(sys.stdin.readline())
W = int(sys.stdin.readline())

result = int((min(H, W)*100) / 2)
print(result)