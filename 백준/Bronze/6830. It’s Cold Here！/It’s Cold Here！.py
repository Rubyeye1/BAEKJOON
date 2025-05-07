import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

c, m = "", 274

try:
    while True:
        tempc, tempm = input().split()

        if int(tempm) < m:
            c = tempc
            m = int(tempm)

except:
    print(c)