import math
import sys
from collections import deque
import copy

L = list(map(int, sys.stdin.readline().split()))
if L[0] == 1 and L[1] == 2 and L[2] == 3 and L[3] == 4 and L[4] == 5 and L[5] == 6 and L[6] == 7 and L[7] == 8:
    print("ascending")
elif L[0] == 8 and L[1] == 7 and L[2] == 6 and L[3] == 5 and L[4] == 4 and L[5] == 3 and L[6] == 2 and L[7] == 1:
    print("descending")
else:
    print("mixed")