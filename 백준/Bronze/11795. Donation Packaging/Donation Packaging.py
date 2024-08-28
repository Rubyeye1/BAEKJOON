import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())
minus = min(a, b, c)

if a >= 30 and b >= 30 and c >= 30:
    print(minus)
    a -= minus
    b -= minus
    c -= minus
else:
    print("NO")

for i in range(T-1):

    tempa, tempb, tempc = map(int, sys.stdin.readline().split())

    a += tempa
    b += tempb
    c += tempc
    minus = min(a,b,c)

    if a >= 30 and b >= 30 and c >= 30:
        print(minus)
        a -= minus
        b -= minus
        c -= minus
    else:
        print("NO")