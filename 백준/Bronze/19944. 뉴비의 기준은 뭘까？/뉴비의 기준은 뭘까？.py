import math
import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
if M == 1 or M == 2:
    print("NEWBIE!")
elif M > 2 and N >= M:
    print("OLDBIE!")
else:
    print("TLE!")