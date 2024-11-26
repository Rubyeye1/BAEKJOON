import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

temp = int(sys.stdin.readline())

if temp % 2 == 0:
    print("Duck")
else:
    print("Goose")