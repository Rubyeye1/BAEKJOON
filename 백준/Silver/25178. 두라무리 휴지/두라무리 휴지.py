import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())
A = input()
B = input()
A = list(A)
B = list(B)

C = A.copy()
D = B.copy()
C.sort()
D.sort()

tempA = []
tempB = []
for i in range(N):
    if A[i] != 'a' and A[i] != 'e' and A[i] != 'i' and A[i] != 'o' and A[i] != 'u':
        tempA.append(A[i])
for i in range(N):
    if B[i] != 'a' and B[i] != 'e' and B[i] != 'i' and B[i] != 'o' and B[i] != 'u':
        tempB.append(B[i])

if C != D:
    print("NO")
elif A[0] != B[0] or A[N-1] != B[N-1]:
    print("NO")
elif tempA != tempB:
    print("NO")
else:
    print("YES")