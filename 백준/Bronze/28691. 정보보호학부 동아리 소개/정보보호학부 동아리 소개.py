import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = input()

if N == "M":
    print("MatKor")
elif N == "W":
    print("WiCys")
elif N == "C":
    print("CyKor")
elif N == "A":
    print("AlKor")
elif N == "$":
    print("$clear")