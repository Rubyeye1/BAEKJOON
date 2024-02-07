import math
import sys

N = int(sys.stdin.readline())
L = set()

result = 0
for i in range(N):
    temp = input()
    if temp == "ENTER":
        result = result + len(L)
        L.clear()
    else:
        L.add(temp)

result = result + len(L)
print(result)