import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

N = int(sys.stdin.readline())

print(math.factorial(N) // (math.factorial(N - 5) * math.factorial(5)))