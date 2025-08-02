import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())

if N % 2 == 0:
    print("I LOVE CBNU")
else:
    print("*" * N)
    print(" " * (N // 2) + "*")

    for i in range(N // 2):
        print(" " * (N // 2 - i - 1) + "*" + " " * (i * 2 + 1) + "*")