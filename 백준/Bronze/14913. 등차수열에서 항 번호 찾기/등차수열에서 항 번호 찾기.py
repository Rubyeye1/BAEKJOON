import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime
import re
import math

a, d, k = map(int, sys.stdin.readline().split())

print((k - a) // d + 1 if (k - a) % d == 0 and (k - a) // d >= 0 else 'X')