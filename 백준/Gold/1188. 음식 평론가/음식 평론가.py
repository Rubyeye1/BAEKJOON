import math
import sys
from collections import deque
import copy
import datetime


N, M = map(int, sys.stdin.readline().split())

print(M - math.gcd(N, M))