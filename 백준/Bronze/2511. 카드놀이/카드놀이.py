import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
tempA = 0
tempB = 0
w = ""

if A == B:
    print(10, 10)
    print("D")

else:
    for i in range(len(A)):
        if A[i] > B[i]:
            tempA += 3
            w = "A"
        elif A[i] == B[i]:
            tempA += 1
            tempB += 1
        elif A[i] < B[i]:
            tempB += 3
            w = "B"

    if tempA == tempB:
        print(tempA, tempB)
        print(w)
        
    else:
        print(tempA, tempB)
        if tempA > tempB:
            print("A")
        elif tempA < tempB:
            print("B")