import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

a = list(map(str, input().split(" ")))

cnt = 0

for i in range(len(a)):
    if a[i].count("ae") >= 1:
        cnt += 1

if cnt / len(a) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")