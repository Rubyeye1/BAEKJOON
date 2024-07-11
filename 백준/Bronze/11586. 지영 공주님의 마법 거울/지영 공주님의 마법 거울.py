import math
import sys
from collections import deque
import copy
import datetime

N = int(sys.stdin.readline())
sysinput = sys.stdin.readline
mirror = [list(sysinput().strip()) for _ in range(N)]
temp = [[0] * N for _ in range(N)]
K = int(sys.stdin.readline())

if K == 1:
    
    for i in range(N):
        for j in range(N):
            print(mirror[i][j],end="")
        print("")
        
elif K == 2:
    
    for i in range(N):
        mirror[i] = mirror[i][::-1]
    for i in range(N):
        for j in range(N):
            print(mirror[i][j],end="")
        print("")
        
elif K == 3:
    
    mirror = mirror[::-1]
    for i in range(N):
        for j in range(N):
            print(mirror[i][j],end="")
        print("")