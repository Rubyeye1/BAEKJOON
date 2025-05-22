import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

S = input()
P = input()

if P in S:
    print(1)
else:
    print(0)