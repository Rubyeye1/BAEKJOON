import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    temp = (m - n + 1) * (n + m) // 2

    print(f"Scenario #{i + 1}:")
    print(f"{temp}\n")