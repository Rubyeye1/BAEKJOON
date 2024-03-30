import math
import sys
from collections import deque
import copy

N = int(input())
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    gcd = math.gcd(a,b)
    lcm = math.lcm(a,b)
    print(lcm, gcd)