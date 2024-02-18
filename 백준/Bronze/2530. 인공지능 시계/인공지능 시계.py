import math
import sys
from collections import deque
import copy


A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())

C = C + D
B = B + int(C/60)
A = A + int(B/60)

print(A % 24, B % 60, C % 60)