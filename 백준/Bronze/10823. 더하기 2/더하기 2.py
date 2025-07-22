import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

S = ''

while True:

    try:
        temp = input()
        S += temp

    except:
        break

print(sum(map(int, S.split(','))))