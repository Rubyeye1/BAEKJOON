import math
import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

T = int(sys.stdin.readline())

for _ in range(T):

    L = list(map(int, sys.stdin.readline().split()))

    result = int(9.23076 * ((26.7 - L[0]) ** 1.835)) + int(1.84523 * ((L[1] - 75) ** 1.348)) + int(56.0211 * ((L[2] - 1.5) ** 1.05)) + int(4.99087 * ((42.5 - L[3]) ** 1.81)) + int(0.188807 * ((L[4] - 210) ** 1.41)) + int(15.9803 * ((L[5] - 3.8) ** 1.04)) + int(0.11193 * ((254 - L[6]) ** 1.88))
    print(result)