import math
import sys
from collections import deque
import copy
import datetime

for i in range(3):

    h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())

    t1 = (h1 * 3600) + (m1 * 60) + s1
    t2 = (h2 * 3600) + (m2 * 60) + s2

    temp = t2 - t1

    resultH = (temp // 60 // 60) % 24
    resultM = (temp // 60) % 60
    resultS = temp % 60
    
    print(resultH, resultM, resultS)