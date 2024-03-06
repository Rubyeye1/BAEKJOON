import math
import sys
from collections import deque
import copy


while True:
    
    A, B  = map(int, sys.stdin.readline().split())
    
    if A == 0 and B == 0:
        break
    
    div = A // B
    A = A - div * B
    print(div, A, "/", B)