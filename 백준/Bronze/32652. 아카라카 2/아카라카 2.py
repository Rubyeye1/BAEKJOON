import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

K = int(sys.stdin.readline())

result = "AKARAKA" + "RAKA" * (K - 1)
print(result)