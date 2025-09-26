import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

P = int(sys.stdin.readline())

for _ in range(P):
    K, N = map(int, sys.stdin.readline().split())
    
    S1 = N * (N + 1) // 2
    S2 = int((N * 2) * (N / 2))
    S3 = int((N * 2 + 2) * (N / 2))

    print(K, S1, S2, S3)
