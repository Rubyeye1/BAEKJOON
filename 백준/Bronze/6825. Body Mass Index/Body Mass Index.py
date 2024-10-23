import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime


w = float(sys.stdin.readline())
h = float(sys.stdin.readline())

bmi = w / (h * h)

if bmi > 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")