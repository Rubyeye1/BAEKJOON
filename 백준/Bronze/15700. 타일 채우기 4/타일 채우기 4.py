import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N, M = map(int, sys.stdin.readline().split())

print((N * M) // 2)