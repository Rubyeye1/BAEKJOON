import math
import sys

N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    for k in range(N-i):
        print(" ", end="")
    for j in range((i*2)-1):
        print("*", end="")
    print("")