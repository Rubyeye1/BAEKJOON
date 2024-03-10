import math
import sys
from collections import deque
import copy

K,D,A = map(int, sys.stdin.readline().split("/"))

if K + A < D or D == 0:
    print("hasu")
else:
    print("gosu")