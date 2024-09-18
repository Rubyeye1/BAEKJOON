import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

if T >= 620 and T <= 780:
    print("Red")
elif T >= 590 and T <= 620:
    print("Orange")
elif T >= 570 and T <= 590:
    print("Yellow")
elif T >= 495 and T <= 570:
    print("Green")
elif T >= 450 and T <= 495:
    print("Blue")
elif T >= 425 and T <= 450:
    print("Indigo")
else:
    print("Violet")