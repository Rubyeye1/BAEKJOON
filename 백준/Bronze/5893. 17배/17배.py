import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
N = int(str(N), 2)
N *= 17

print(bin(N)[2:])