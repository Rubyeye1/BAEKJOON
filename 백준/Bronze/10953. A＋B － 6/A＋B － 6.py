import math
import sys
from collections import deque
import copy

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split(","))
    print(A+B)