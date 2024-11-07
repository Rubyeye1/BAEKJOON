import sys
from collections import deque
import copy
import datetime
import math
from datetime import date, datetime

Vk, Jk = map(int, sys.stdin.readline().split())
Vj, Jj = map(int, sys.stdin.readline().split())
Vh, Dh, Jh = map(int, sys.stdin.readline().split())

temp = Vh * Dh * Jh

print(Vk * Jk * temp + Vj * Jj * temp)