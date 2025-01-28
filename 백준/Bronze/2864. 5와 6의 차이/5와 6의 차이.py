import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

A, B = map(str, sys.stdin.readline().split())

A = list(A)
B = list(B)
C = A.copy()
D = B.copy()

for i in range(len(A)):
    if A[i] == "6":
        A[i] = "5"
for i in range(len(B)):
    if B[i] == "5":
        B[i] = "6"
for i in range(len(C)):
    if C[i] == "5":
        C[i] = "6"
for i in range(len(D)):
    if D[i] == "6":
        D[i] = "5"

tempA = ''.join(map(str, A))
tempB = ''.join(map(str, B))
tempC = ''.join(map(str, C))
tempD = ''.join(map(str, D))
tempA = int(tempA)
tempB = int(tempB)
tempC = int(tempC)
tempD = int(tempD)

print(tempA+tempD, tempB+tempC)