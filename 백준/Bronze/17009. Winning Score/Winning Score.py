import math
import sys
from collections import deque
import copy

A = []
B = []
for i in range(3):
    temp = int(input())
    A.append(temp)
for i in range(3):
    temp = int(input())
    B.append(temp)


if ((A[0] * 3) + (A[1] * 2) + (A[2] * 1)) > ((B[0] * 3) + (B[1] * 2) + (B[2] * 1)):
    print('A')
elif ((A[0] * 3) + (A[1] * 2) + (A[2] * 1)) < ((B[0] * 3) + (B[1] * 2) + (B[2] * 1)):
    print('B')
else:
    print('T')