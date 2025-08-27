import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A, B, C, D = map(int, sys.stdin.readline().split())

print(abs((A + D) - (B + C)))