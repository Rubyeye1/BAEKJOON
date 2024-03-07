import math
import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
S = input()
S = list(S)

result = 0
bonus = 0

for i in range(len(S)):
    if i == 0:
        if S[i] == "O":
            result = result + 1
            bonus = bonus + 1
            continue
        else:
            continue
    else:
        if S[i] == "O":
            if S[i-1] == "O":
                result = result + (i+1)
                result = result + bonus
                bonus = bonus + 1
            elif S[i-1] == "X":
                result = result + (i+1)

                bonus = bonus + 1
        else:
            bonus = 0

print(result)