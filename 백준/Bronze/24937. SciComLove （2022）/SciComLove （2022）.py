import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


N = int(sys.stdin.readline()) % 10
temp = 'SciComLove'

result = temp[N:] + temp[:N]
print(result)