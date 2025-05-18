import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = b - a

if c <= 0:
    print("Congratulations, you are within the speed limit!")
elif c >= 1 and c <= 20:
    print("You are speeding and your fine is ${}.".format(100))
elif c >= 21 and c <= 30:
    print("You are speeding and your fine is ${}.".format(270))
elif c >= 31:
    print("You are speeding and your fine is ${}.".format(500))