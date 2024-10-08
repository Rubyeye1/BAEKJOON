import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

N = int(sys.stdin.readline())

L = list(map(str, input().split()))
Hello = input()

print(L.count(Hello))