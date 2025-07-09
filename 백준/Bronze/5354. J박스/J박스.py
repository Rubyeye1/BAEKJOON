import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime
import re

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    if N < 3:
        for i in range(N):
            print('#' * N)

        print()
    else:
        print('#' * N)

        for i in range(N - 2):
            print('#' + 'J' * (N - 2) + '#')

        print('#' * N)
        print()