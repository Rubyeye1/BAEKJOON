import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

N = int(sys.stdin.readline())
stt = int(sys.stdin.readline())

if N % 4 == 0:
    if N % 100 == 0:
        if N % 400 == 0:
            print(30)
        else:
            print(29)
    else:
        print(30)
else:
    print(29)