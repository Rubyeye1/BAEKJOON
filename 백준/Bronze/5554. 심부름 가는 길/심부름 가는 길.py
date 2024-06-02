import math
import sys
from collections import deque
import copy
import datetime

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

temp = a+b+c+d
x = temp // 60
y = temp % 60
print(x,y)