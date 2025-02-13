import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):

    a, b = map(str, input().split())
    c = a
    d = b

    a = list(a)
    b = list(b)

    a.sort()
    b.sort()

    if a == b:
        print(c + " & " + d + " are anagrams.")
    else:
        print(c + " & " + d + " are NOT anagrams.")