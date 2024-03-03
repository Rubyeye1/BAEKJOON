import math
import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())

result = 0
L = []
for i in range(J):
    temp = int(sys.stdin.readline())
    L.append(temp)
baguniMin = 1
baguniMax = M

for apple in L:

    if apple >= baguniMin and apple <= baguniMax:
        continue

    elif apple < baguniMin:

        result = result + baguniMin - apple
        baguniMax = baguniMax - (baguniMin - apple)
        baguniMin = apple

    elif apple > baguniMax:

        result = result + apple - baguniMax
        baguniMin = baguniMin + (apple - baguniMax)
        baguniMax = apple


print(result)