import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
for i in range(N):
    a = input().split(" ")
    a.reverse()
    print("Case #" + str(i+1) + ": ", end="")
    for j in range(len(a)):
        print(a[j], end=" ")