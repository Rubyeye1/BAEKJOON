import math
import sys
from collections import deque
import copy
import datetime


N = int(sys.stdin.readline())

if N == 1:
    print(" " * (N-1) + "*")
else:
    print(" " * (N-1) + "*")
    for i in range(1, N-1):
        print(" " * (N-(i+1)) + "*" + " " * ((i*2) -1) + "*")
    print("*" * ((N*2)-1))