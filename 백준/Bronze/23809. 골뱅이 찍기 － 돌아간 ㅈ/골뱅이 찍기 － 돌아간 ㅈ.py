import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

for _ in range(N):
    print(("@" * N) + (" " * (N * 3)) + ("@" * N))

for _ in range(N):
    print(("@" * N) + (" " * (N * 2)) + ("@" * N))

for _ in range(N):
    print("@" * (N * 3))

for _ in range(N):
    print(("@" * N) + (" " * (N * 2)) + ("@" * N))

for _ in range(N):
    print(("@" * N) + (" " * (N * 3)) + ("@" * N))