import math
import sys
from collections import deque
import copy
import datetime

S = input()
happyCount = S.count(":-)")
sadCount = S.count(":-(")

if happyCount == 0 and sadCount == 0:
    print("none")
elif happyCount == sadCount:
    print("unsure")
elif happyCount > sadCount:
    print("happy")
else:
    print("sad")