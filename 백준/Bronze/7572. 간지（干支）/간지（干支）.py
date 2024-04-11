import math
import sys
from collections import deque
import copy
import datetime

N = int(input())
temp = N % 60

temp = temp - 4

a = int(temp % 10)
b = int(temp % 12)

if a == 0:
    resultA = "0"
elif a == 1:
    resultA = "1"
elif a == 2:
    resultA = "2"
elif a == 3:
    resultA = "3"
elif a == 4:
    resultA = "4"
elif a == 5:
    resultA = "5"
elif a == 6:
    resultA = "6"
elif a == 7:
    resultA = "7"
elif a == 8:
    resultA = "8"
elif a == 9:
    resultA = "9"

if b == 0:
    resultB = "A"
elif b == 1:
    resultB = "B"
elif b == 2:
    resultB = "C"
elif b == 3:
    resultB = "D"
elif b == 4:
    resultB = "E"
elif b == 5:
    resultB = "F"
elif b == 6:
    resultB = "G"
elif b == 7:
    resultB = "H"
elif b == 8:
    resultB = "I"
elif b == 9:
    resultB = "J"
elif b == 10:
    resultB = "K"
elif b == 11:
    resultB = "L"

print(resultB+resultA)