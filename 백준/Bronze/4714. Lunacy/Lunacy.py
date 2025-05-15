import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

while True:
    f = float(sys.stdin.readline())
    if f == -1.0:
        break

    print("Objects weighing %.2f on Earth will weigh %.2f on the moon." % (f, f * 0.167))   