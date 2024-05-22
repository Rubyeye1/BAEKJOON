import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    for j in range(i-1):
        print(" ", end="")
    for k in range(N-(i-1)):
        print("*", end="")
    print("")
for i in range(2*N-1 -(N)):
    for j in range(i+1):
        print(" ",end="")
    for k in range(2*N-1 -(N) - i):
        print("*",end="")
    print("")