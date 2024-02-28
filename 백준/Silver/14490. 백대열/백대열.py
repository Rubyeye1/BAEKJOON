import math
import sys
from collections import deque
import copy

N, M = map(int, input().split(':'))
result = math.gcd(N, M)
print(int(N // result), end="")
print(':', end="")
print(int(M // result))