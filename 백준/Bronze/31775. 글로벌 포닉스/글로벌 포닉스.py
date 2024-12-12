import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

S1 = input()
S2 = input()
S3 = input()

resultL = 0
resultK = 0
resultP = 0

if S1[0] == "l":
    resultL += 1
elif S1[0] == "k":
    resultK += 1
elif S1[0] == "p":
    resultP += 1

if S2[0] == "l":
    resultL += 1
elif S2[0] == "k":
    resultK += 1
elif S2[0] == "p":
    resultP += 1

if S3[0] == "l":
    resultL += 1
elif S3[0] == "k":
    resultK += 1
elif S3[0] == "p":
    resultP += 1

if resultL == 1 and resultK == 1 and resultP == 1:
    print("GLOBAL")
else:
    print("PONIX")