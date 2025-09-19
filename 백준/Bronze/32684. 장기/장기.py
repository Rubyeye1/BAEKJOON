import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

ce = list(map(int, sys.stdin.readline().split()))
eg = list(map(int, sys.stdin.readline().split()))

cetemp = ce[0] * 13 + ce[1] * 7 + ce[2] * 5 + ce[3] * 3 + ce[4] * 3 + ce[5] * 2
egtemp = eg[0] * 13 + eg[1] * 7 + eg[2] * 5 + eg[3] * 3 + eg[4] * 3 + eg[5] * 2 + 1.5

if cetemp > egtemp:
    print("cocjr0208")
else:
    print("ekwoo")