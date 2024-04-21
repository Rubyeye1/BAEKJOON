import math
import sys
from collections import deque
import copy
import datetime



for i in range(3):
    Max = 0
    count = 0

    S = int(input())
    S = list(map(int, str(S)))

    for j in range(1, 8):
        if S[j-1] == S[j]:
            if j == 7:
                count += 2
                Max = max(Max, count)
            count += 1
        else:
            count += 1
            Max = max(Max, count)
            count = 0


    print(Max)