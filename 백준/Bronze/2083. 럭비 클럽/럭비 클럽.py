import math
import sys
from collections import deque
import copy
import datetime
from datetime import date, datetime


while True:

    N, A, K = map(str, sys.stdin.readline().split())
    A = int(A)
    K = int(K)
    
    if N == "#":
        break

    if A > 17 or K >= 80:
        print(N + " Senior")
    else:
        print(N + " Junior")