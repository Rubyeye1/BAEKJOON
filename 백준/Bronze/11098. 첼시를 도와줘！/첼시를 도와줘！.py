import math
import sys
from collections import deque
import copy
import datetime

n = int(sys.stdin.readline())
for i in range(n):

    p = int(sys.stdin.readline())
    
    Price = []
    Name = []

    for j in range(p):
        
        a, b = input().split()
        
        Price.append(int(a))
        Name.append(b)

    print(Name[Price.index(max(Price))])