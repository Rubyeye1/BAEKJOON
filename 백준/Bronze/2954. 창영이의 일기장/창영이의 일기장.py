import math
import sys
from collections import deque
import copy
import datetime

S = input()
result = []
count = 0
for i in range(len(S)):
    if count == 1:
        count += 1
        continue
    if count == 2:
        count = 0
        continue
    if S[i] == 'a' or S[i] == 'e' or S[i] == 'i' or S[i] == 'o' or S[i] == 'u':
        result.append(S[i])
        count = 1
    else:
        result.append(S[i])
        count = 0

for i in range(len(result)):
    print(result[i], end="")