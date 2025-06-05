import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
apple = 0
box = 0

for _ in range(N):
    T, W, H, L = map(str, input().split())
    W = int(W)
    H = int(H)
    L = int(L)

    if T == "A":
        apple += (W // 12) * (H // 12) * (L // 12)
        box += 1000
    else:
        box += 6000

print(apple * 500 + box)
print(apple * 4000) 