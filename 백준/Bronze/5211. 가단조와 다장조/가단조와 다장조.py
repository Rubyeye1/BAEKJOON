import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

L = list(map(str, input().split("|")))
resultD = 0
resultK = 0

for i in range(len(L)):
    if L[i][0] == "C" or L[i][0] == "F" or L[i][0] == "G":
        resultD += 1
    elif L[i][0] == "A" or L[i][0] == "D" or L[i][0] == "E":
        resultK += 1

if resultD > resultK:
    print("C-major")
elif resultK > resultD:
    print("A-minor")
elif resultD == resultK:
    if L[-1][-1] == "C" or L[-1][-1] == "F" or L[-1][-1] == "G":
        print("C-major")
    elif L[-1][-1] == "A" or L[-1][-1] == "D" or L[-1][-1] == "E":
        print("A-minor")