import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re


T = input()

result = set(re.findall(r'\d+', T))

print(len(result))